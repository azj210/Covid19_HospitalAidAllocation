import urllib.request as request
import csv
from collections import defaultdict
from datetime import date
from datetime import date, timedelta


def editDict(dict, link):
	#loop through the file and add the [confirmed,deaths] as a value to key county,state in dict
	r = request.urlopen(link).read().decode('utf8').split("\n")
	reader = csv.reader(r)
	stillUS = True
	for line in reader:
		if len(line) > 2 and line[1] != 'Admin2' and line[1] != '' and line[1] != 'Unassigned' and line[1] != 'unassigned':
			#line[7] is confirmed and line[8] is deaths
			dict[line[1] + ', ' + line[2]].append([line[7],line[8]])

def main():
	#set datetime
    print("a")
    start = date(2020,3,22)
    end = date.today()
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
            print(i, tracker[i])
            print(len(tracker[i]))
    
if __name__ == '__main__':
	main()











