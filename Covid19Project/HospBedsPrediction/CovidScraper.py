import urllib.request as request
import csv
from collections import defaultdict, OrderedDict
from datetime import date, timedelta
import numpy as np
import copy
import json

def editDict(dictInput, link):
    #loop through the file and add the [confirmed,deaths] as a value to key county,state in dict
    r = request.urlopen(link).read().decode('utf8').split("\n")
    reader = csv.reader(r)
    for line in reader:
        if len(line) > 2 and line[1] == "New York City":
            dictInput["new york" + ',' + line[2].lower()].append([line[7],line[8]])
        elif len(line) > 2 and line[1] != 'Admin2' and line[1] != '' and line[1] != 'Unassigned' and line[1] != 'unassigned' and line[3] == 'US':
            #line[7] is confirmed and line[8] is deaths
            dictInput[line[1].lower() + ',' + line[2].lower()].append([line[7],line[8]])

def predict(x, y, pred):
    #quadratic regression: predicting cases for pred days out
    coeffs = np.polyfit(x, y, 2)
    futureCases = []
    for i in range(len(x), len(x)+pred):
        case = int(round((coeffs[0] * (i**2)) + (coeffs[1] * i) + coeffs[1]))
        if case <= 0:
            futureCases.append(0)
        else:
            futureCases.append(case)
    return futureCases

def generatePredict(tracker, condition, days):
    res = defaultdict(int)
    for i in tracker.keys():
        #error handling for if there is 2 days or less worth of data
        if len(tracker[i]) > 2:
            data = tracker[i]
            time = [t for t in range (1, len(tracker[i]))]
            cases = []
            if condition == "cases":
                for j in range(1, len(data)):
                    cases.append(max(0,(int(data[j][0]) - int(data[j-1][0]))))
            else:
                for j in range(1, len(data)):
                    cases.append(max(0,(int(data[j][1]) - int(data[j-1][1]))))  
            #calculate number of new cases or deaths "days" days out
            futureCases = predict(time, cases, days)
            cases += futureCases
            res[i] = cases
    return res

#c - time series of new cases from 3/22 to "days" days from the end date. d is corresponding new death time series
def bedsNeeded(c, d, tracker, days):
    beds = defaultdict(list)
    dischargeAmt = {15:(1/4), 21:(1/3), 26:(1/2), 32:1}
    #run simulation for each county
    for i in c.keys():
        #Of the initial reported numbers, around 75% are in the hospital
        beds[i].append(int(round(int(tracker[i][0][0]) * .75)))
        #1/3 of people need hospitalization and of those 1/3%, it can be assumed that 75% will be discharged
        toDischarge = [round(z * (1/3) * 0.75) for z in copy.deepcopy(c[i])] 
        #loop through all days from day 1 to today
        for j in range(len(c[i])):
            yestH, newHosp, deaths = beds[i][j], (1/3) * c[i][j], 0.8 * d[i][j] 
            #calculate people to discharge today
            todayDischarge = 0
            for k in dischargeAmt.keys():
                if j >= k:
                    #discharge dischargeAmt[k] people from k days ago
                    discharge = dischargeAmt[k] * (toDischarge[j-k])
                    todayDischarge += discharge
                    toDischarge[j-k] -= discharge
            beds[i].append(max(0,(int(round(yestH + newHosp - deaths - todayDischarge)))))
        if len(beds[i]) > days:
            beds[i].remove(beds[i][0])
        if len(beds[i]) < days:
            extra = [0] * (days - len(beds[i]))
            beds[i] = extra + beds[i]
    return beds

def main():
    start, end, delta = date(2020,3,22), date(2020,4,25), timedelta(days=1)
    tracker = defaultdict(list)
    days, days2 = 3, 3
    dates = []
	#loop through all available covid files from 3/22/2020 to today
    while start <= end:
        thisDate = start.strftime('%m-%d-%Y')
        dates.append(thisDate)
        link = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + thisDate + '.csv'
        editDict(tracker, link)
        start += delta
        days += 1
    for i in range(days2):
        dates.append(start.strftime('%m-%d-%Y'))
        start += delta
    c, d = generatePredict(tracker, "cases", days2), generatePredict(tracker, "deaths", days2)
    b = bedsNeeded(c, d, tracker, days)
    #converting bedsNeeded to json to read into spark dataframe
    forwJson = []
    for i in b.keys():
        place = i.split(",")
        toAppend = OrderedDict()
        toAppend["county"], toAppend["state"] = place[0], place[1]
        for j in range(len(b[i])):
            toAppend[dates[j]] = b[i][j]
        forwJson.append(toAppend)
    with open('BedsNeeded.json', mode='w+') as output:
        json.dump(forwJson,output)

if __name__ == '__main__':
	main()











