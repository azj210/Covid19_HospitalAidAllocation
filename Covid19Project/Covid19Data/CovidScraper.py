import urllib.request as request
import csv
from collections import defaultdict
from datetime import date
from datetime import date, timedelta
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def editDict(dict, link):
	#loop through the file and add the [confirmed,deaths] as a value to key county,state in dict
	r = request.urlopen(link).read().decode('utf8').split("\n")
	reader = csv.reader(r)
	stillUS = True
	for line in reader:
		if len(line) > 2 and line[1] != 'Admin2' and line[1] != '' and line[1] != 'Unassigned' and line[1] != 'unassigned':
			#line[7] is confirmed and line[8] is deaths
			dict[line[1] + ', ' + line[2]].append([line[7],line[8]])

#linear regression
def bestFit(x, y):
    xMean = sum(x)/len(x)
    yMean = sum(y)/len(y)
    numer = sum([xi*yi for xi,yi in zip(x, y)]) - len(x) * xMean * yMean
    denom = sum([xi**2 for xi in x]) - len(x) * xMean**2
    b = numer / denom
    a = yMean - b * xMean
    print('Best Fit Line:\ny = {:.2f} + {:.2f}x'.format(a, b))
    return a, b

#polynomial regression

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
            #cumulative cases and deaths
            """
            time = [i for i in range (len(tracker[i]))]
            cases = [int(i[0]) for i in data]
            deaths = [int(i[1]) for i in data]
            #print(i, tracker[i])
            plt.plot(time, cases)
            plt.xlabel('Time (day)')
            plt.ylabel('Cases')
            plt.plot(time, deaths)
            plt.xlabel('Time (day)')
            plt.ylabel('Deaths')
            """
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
            """
            print(time)
            print(cases)
            print(deaths)
            plt.plot(time, cases)
            plt.xlabel('Time (day)')
            plt.ylabel('Cases')
            plt.plot(time, deaths)
            plt.xlabel('Time (day)')
            plt.ylabel('Deaths')
            """
            #first calculate number of cases 
            #time in relation to cases
            a = Polynomial.fit(time, cases, 2)
            plt.plot(*a.linspace())

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











