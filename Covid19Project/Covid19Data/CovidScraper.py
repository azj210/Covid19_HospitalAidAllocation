import urllib.request as request
import csv
from collections import defaultdict
from datetime import date
from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial

def editDict(dictInput, link):
	#loop through the file and add the [confirmed,deaths] as a value to key county,state in dict
	r = request.urlopen(link).read().decode('utf8').split("\n")
	reader = csv.reader(r)
	#stillUS = True
	for line in reader:        
		if len(line) > 2 and line[1] != 'Admin2' and line[1] != '' and line[1] != 'Unassigned' and line[1] != 'unassigned':
			#line[7] is confirmed and line[8] is deaths
			dictInput[line[1] + ', ' + line[2]].append([line[7],line[8]])
#regression
def predict(x, y, dim, pred):
    # Find the slope and intercept of the best fit line
    if dim == 2:
        #predicting cases 4 days out
        #quadratic regression
        coeffs = np.polyfit(x, y, dim)
        futureCases = []
        for i in range(len(x),len(x)+4):
            case = (coeffs[0] * (i**2)) + (coeffs[1] * i) + coeffs[1]
            if case <= 0:
                futureCases.append(0)
            else:
                futureCases.append(case)
        return futureCases
    else:
        #predicting deaths for predicted cases
        #linear regression
        coeffs2 = np.polyfit(x, y, dim)
        deaths = (coeffs2[0] * pred) + coeffs2[1]
        if deaths <= 0:
            return 0
        else:
            return ((coeffs2[0] * pred) + coeffs2[1])

def main():
	#set datetime
    start = date(2020,3,22)
    end = date(2020, 4,18)
    #end = date.today()
    delta = timedelta(days=1)
    tracker = defaultdict(list)
	#loop through covid files from 3/22/2020 to today
	#note: use the previous day if today's file has not been uploaded yet
    while start <= end:
        thisDate = start.strftime('%m-%d-%Y')
        link = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + thisDate + '.csv'
        editDict(tracker, link)
        start += delta
    for i in tracker.keys():
        #print(i, tracker[i])
        #print("\n")
        if i == "New York City, New York":
            data = tracker[i]
            time = [i for i in range (1,len(tracker[i]))]
            #new cases and deaths
            cases = []
            deaths = []
            for i in range(1,len(data)):
                cases.append(int(data[i][0]) - int(data[i-1][0]))
                deaths.append(int(data[i][1]) - int(data[i-1][1]))
            #take into account lag between cases and deaths
            lagCases = cases[:len(cases)-2]
            lagDeaths = deaths[2:]
            #first calculate number of new cases 4 days out
            #time in relation to cases
            a = Polynomial.fit(time, cases, 2)
            plt.plot(*a.linspace())
            newCases = predict(time, cases, 2, 0)
            
            #next calculate number of new deaths each of the 4 days
            for i in newCases:
                print(predict(lagCases, lagDeaths, 1, i))
            

            """
            #cases in relation to deaths
            p = Polynomial.fit(lagCases, lagDeaths, 1)
            plt.plot(*p.linspace())
            plt.scatter(lagCases,lagDeaths)            
            #input cases into x to generate y - deaths. Floor for deaths is 0
            print(bestFit(lagCases,lagDeaths))
            """


if __name__ == '__main__':
	main()











