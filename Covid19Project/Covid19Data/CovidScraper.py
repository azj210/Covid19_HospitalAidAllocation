import urllib.request as request
import csv
from collections import defaultdict, OrderedDict
from datetime import date, timedelta
import numpy as np
import copy
import json
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

def editDict(dictInput, link):
    #loop through the file and add the [confirmed,deaths] as a value to key county,state in dict
    r = request.urlopen(link).read().decode('utf8').split("\n")
    reader = csv.reader(r)
    for line in reader:
        if len(line) > 2 and line[1] == "New York City":
            dictInput["new york" + ', ' + line[2].lower()].append([line[7],line[8]])
        elif len(line) > 2 and line[1] != 'Admin2' and line[1] != '' and line[1] != 'Unassigned' and line[1] != 'unassigned' and line[3] == 'US':
            	#line[7] is confirmed and line[8] is deaths
            dictInput[line[1].lower() + ', ' + line[2].lower()].append([line[7],line[8]])

def predict(x, y, pred):
    #quadratic regression: predicting cases 3 days out
    coeffs = np.polyfit(x, y, 2)
    futureCases = []
    for i in range(len(x),len(x)+pred):
        case = int(round((coeffs[0] * (i**2)) + (coeffs[1] * i) + coeffs[1]))
        if case <= 0:
            futureCases.append(0)
        else:
            futureCases.append(case)
    return futureCases

def generatePredict(tracker, condition, writer):
    iCases = defaultdict(int)
    iDeaths = defaultdict(int)
    for i in tracker.keys():
        place = i.split(",")
        #error handling for if there is 2 days or less worth of data
        if len(tracker[i]) > 2:
            data = tracker[i]
            time = [t for t in range (1,len(tracker[i]))]
            if condition == "cases":
                #new cases 
                cases = []
                for j in range(1,len(data)):
                    cases.append(max(0,(int(data[j][0]) - int(data[j-1][0]))))
                #calculate number of new cases 3 days out
                futureCases = predict(time, cases, 3)
                writer.writerow([place[0],place[1]] + futureCases)
                cases += futureCases
                iCases[i] = cases
            else:
                deaths = []
                for j in range(1,len(data)):
                    deaths.append(max(0,(int(data[j][1]) - int(data[j-1][1]))))  
                futureDeaths = predict(time, deaths, 3)
                writer.writerow([place[0],place[1]] + futureDeaths)
                deaths += futureDeaths
                iDeaths[i] = deaths
    if condition == "cases":
        return iCases
    else:
        return iDeaths

#c - time series of new cases from 3/22 to 3 days from the end date. d is corresponding new death time series
def bedsNeeded(c, d, tracker, days, writer):
    beds = defaultdict(list)
    #run simulation for each county
    for i in c.keys():
        place = i.split(",")
        beds[i].append(int(round(int(tracker[i][0][0]) * .8)))
        #beds[i].append(c[i][0])
        toDischarge = copy.deepcopy(c[i])
        #loop through all days from day 1 to today
        for j in range(len(c[i])):
            yestH = beds[i][j-1]
            newHosp = 0.35 * c[i][j]
            deaths = 0.80 * d[i][j]
            #calculate people to discharge today
            if j >= 7:
                toDischarge[j-7] -= deaths
            todayDischarge = 0
            if j >= 15:
                #discharge 1/4 people from 15 days ago
                discharge =  (1/4) * (toDischarge[j-15])
                todayDischarge += discharge
                toDischarge[j-15] -= discharge
            if j >= 21:
                #discharge 1/3 people from 21 days ago
                discharge =  (1/3) * (toDischarge[j-21])
                todayDischarge += discharge
                toDischarge[j-21] -= discharge
            if j >= 26:
                #discharge 1/2 people from 26 days ago
                discharge =  (1/2) * (toDischarge[j-26])
                todayDischarge += discharge
                toDischarge[j-26] -= discharge
            if j >= 32:
                #discharge remaining people from 31 days ago
                discharge = toDischarge[j-31]
                todayDischarge += discharge
                toDischarge[j-21] = 0
            beds[i].append(max(0,(int(round(yestH + newHosp - deaths - todayDischarge)))))
        if len(beds[i]) > days:
            beds[i].remove(beds[i][0])
        if len(beds[i]) < days:
            extra = [0] * (days - len(beds[i]))
            beds[i] = extra + beds[i]
        writer.writerow([place[0],place[1]] + beds[i])     
    return beds

def main():
    start = date(2020,3,22)
    end = date(2020,4,22)
    delta = timedelta(days=1)
    tracker = defaultdict(list)
    days = 3
    dates = []
	#loop through all available covid files from 3/22/2020 to today
    while start <= end:
        thisDate = start.strftime('%m-%d-%Y')
        dates.append(thisDate)
        link = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + thisDate + '.csv'
        editDict(tracker, link)
        start += delta
        days += 1
    for i in range(3):
        dates.append(start.strftime('%m-%d-%Y'))
        start += delta
    reverseDates = copy.deepcopy(dates)
    reverseDates.reverse()
    with open('PredictCases.csv', mode='w+') as f:
        writer = csv.writer(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        c = generatePredict(tracker, "cases", writer)   
    with open('PredictDeaths.csv', mode='w+') as f:
        writer = csv.writer(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        d = generatePredict(tracker, "deaths", writer)
    #print(tracker["new york, new york"])
    #print(d["new york, new york"])
    with open('PredictBeds.csv', mode='w+') as f:
        writer = csv.writer(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        b = bedsNeeded(c, d, tracker, days, writer)
    #converting bedsNeeded to json
    forwJson = []
    revJson = []
    for i in b.keys():
        #if i == "new york, new york":
        count = 0
        revCount = len(b[i]) - 1
        place = i.split(",")
        toAppend = OrderedDict()
        toAppend["county"] = place[0]
        toAppend["state"] = place[1]
        toReverse = OrderedDict()
        toReverse["county"] = place[0]
        toReverse["state"] = place[1]
        for j in b[i]:
            toAppend[dates[count]] = j
            toReverse[dates[revCount]] = b[i][revCount]
            count += 1
            revCount -= 1
        forwJson.append(toAppend)
        revJson.append(toReverse)
    print(forwJson[0])
    print(revJson[0])
    with open('BedsNeeded.txt', mode='w+') as output:
        json.dump(forwJson,output)
    with open('ReverseBedsNeeded.txt', mode='w+') as output:
        json.dump(revJson,output)    
                
if __name__ == '__main__':
	main()











