import csv


with open("ComplicationsAndDeaths.csv") as csv_file:

	end = 0
	csv_reader = csv.reader(csv_file, delimiter = ',')

	#main 3 repiratory causes of patient death
	causes = ["Death rate for COPD patients", "Death rate for pneumonia patients", "Postoperative Respiratory Failure Rate"]
	#counter for total deaths
	deaths = 0
	#counter for total cases
	denom = 0


	for row in csv_reader:
		if row[9] in causes:
			if row[11] != "Not Available" and row[12] != "Not Available":
				deaths += float(row[11]) * float(row[12]) * 0.01
				denom += float(row[11])

	total = deaths/denom
	print(total)





