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
    for i in tracker.keys():
        if len(tracker[i]) > 2:
            data = tracker[i]
            time = [t for t in range (1,len(tracker[i]))]
            #new cases and new deaths
            cases = []
            deaths = []
            for j in range(1,len(data)):
                cases.append(int(data[j][0]) - int(data[j-1][0]))
                deaths.append(int(data[j][1]) - int(data[j-1][1]))         
            #first calculate number of new cases 4 days out
            newCases = predict(time, cases, 4)
            newDeaths = predict(time, deaths, 4)
            print(i, newCases, newDeaths)
        #error handling for if there is 1 week or less worth of data
        else:
            print(i, [0]*4, [0]*4)

if __name__ == '__main__':
	main()











