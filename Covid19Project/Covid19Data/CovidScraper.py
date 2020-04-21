import urllib.request as request
import csv
from collections import defaultdict
from datetime import date, timedelta
import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

def editDict(dictInput, link):
	#loop through the file and add the [confirmed,deaths] as a value to key county,state in dict
	r = request.urlopen(link).read().decode('utf8').split("\n")
	reader = csv.reader(r)
	for line in reader:        
		if len(line) > 2 and line[1] != 'Admin2' and line[1] != '' and line[1] != 'Unassigned' and line[1] != 'unassigned' and line[3] == 'US':
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
    for i in tracker.keys():
        if i == "new york city, new york":
            place = ["new york", "new york"]
        else:
            place = i.split(",")
        if len(tracker[i]) > 2:
            data = tracker[i]
            time = [t for t in range (1,len(tracker[i]))]
            if condition == "cases":
                #new cases 
                cases = []
                for j in range(1,len(data)):
                    cases.append(int(data[j][0]) - int(data[j-1][0]))
                #calculate number of new cases 4 days out
                writer.writerow([place[0],place[1]] + predict(time, cases, 4))
            else:
                deaths = []
                for j in range(1,len(data)):
                    deaths.append(int(data[j][1]) - int(data[j-1][1]))         
                writer.writerow([place[0],place[1]] + predict(time, deaths, 4))
        #error handling for if there is 2 days or less worth of data
        else:
            writer.writerow([place[0],place[1]] + [0]*4)

def main():
    start = date(2020,3,22)
    end = date(2020,4,20)
    delta = timedelta(days=1)
    tracker = defaultdict(list)
	#loop through covid files from 3/22/2020 to today
    allDates = []
    while start <= end:
        thisDate = start.strftime('%m-%d-%Y')
        link = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + thisDate + '.csv'
        editDict(tracker, link)
        allDates.append(thisDate)
        start += delta
    predDates = []
    for i in range(4):
        end += delta
        predDates.append(end.strftime('%m-%d-%Y'))
        allDates.append(end.strftime('%m-%d-%Y'))
    with open('predictCases.csv', mode='w+') as f:
        writer = csv.writer(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        generatePredict(tracker, "cases", writer)
    with open('predictDeaths.csv', mode='w+') as f:
        writer = csv.writer(f, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        generatePredict(tracker, "deaths", writer)
            

if __name__ == '__main__':
	main()











