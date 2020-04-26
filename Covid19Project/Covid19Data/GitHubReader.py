import urllib.request as request
import csv

#change the date at the end of the csv file name to get the most up to date covid19 data
r = request.urlopen('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-25-2020.csv').read().decode('utf8').split("\n")
reader = csv.reader(r)


with open('CovidData.csv', mode='w+') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in reader:
    	writer.writerow(line)






