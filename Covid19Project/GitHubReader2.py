import urllib.request as request
import csv

r = request.urlopen('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv').read().decode('utf8').split("\n")
reader = csv.reader(r)


with open('CovidConfirms.csv', mode='w+') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in reader:
    	writer.writerow(line)





