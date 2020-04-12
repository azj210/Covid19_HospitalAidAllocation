# Covid19_HospitalAidAllocation
**Goal of Project:**
Examine hospital quality and bed data sets in comparison to Covid19 and US demographics data to reach conclusion on hospital aid allocation by county
MapReduce code for each dataset is found in their respective folders. Note that CountRecs is not part of the analytics, rather it is MapReduce to check the number of lines in input and output files.

**Census**

Census Data was taken in the “Annual County Resident Population Estimates by Age, Sex, Race, and Hispanic Origin: April 1, 2010 to July 1, 2018 (CC-EST2018-ALLDATA)” section under United States from: 
https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html#par_textimage_1383669527

**Covid19**

Under Covid19Data use GitHubReader.py to scrape raw data to a csv file. Change data in the url for the most recent Covid19 data. 
Link to Covid19 data if needed: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

**Hospital Complications and Deaths**

Data was taken under “Download CSV Flat Files” from: https://data.medicare.gov/data/hospital-compare. Within the downloaded files use the “ComplicationsAndDeaths” file. 

**Hospital Beds**

Hospital beds data was taken from: https://www.ahd.com/state_statistics.html. 



**Final Data Schema after Cleaning**
Census
- County: String
- State: String
- Population: int
- MalePopulation: int

