# Covid19_HospitalAidAllocation
link to webpage: http://covidstatusnow.com/


**Goal of Project:**
Examine hospital quality and bed data sets in comparison to Covid19 and US demographics data to reach conclusion on hospital aid allocation by county and general Covid19 data.


**Hadoop MapReduce Portion**

Hadoop MapReduce code for each dataset is found in their respective folders. 

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



**Final Data Schema after Hadoop MapReduce**

Census
- County: String
- State: String
- Population: int
- MalePopulation: int

Covid19
- County: String
- State: String
- Cases: int
- Deaths: int
- Deathrate: float

HospitalComplicationsAndDeaths
- City: String
- County: String
- State: String
- Quality: double

HospitalBeds
- City: String
- State: String
- Beds: int

Results from MapReduce were stored in HDFS. These files were then joined with Hive. Analytics were done on on the joined table table with Impala. SQL code is available under the Analytics folder.


**Hospital Bed Prediction Portion**

Explanation of CovidScraper.py to calculate/predict Hospital Beds Needed Timeseries:

After calculating new cases/deaths every day for each county starting from 3/22, I took the calculated data and fit the data set using a least squares polynomial fit function with days as the independent variable and cases or deaths as the dependent variable. Taking the coefficients that minimize squared error, I used the resultant equation to predict new cases/deaths 3 days out based on days since 3/22.

To calculate Hospital Beds Needed I used a basic formula of: TodayBedsRequired = YesterdayBedsRequired + NewCases * 0.3 - Deaths * 0.8 - Discharges. Of the initial 3/22 numbers, I set initial TodayBedsRequired as 0.75*cases on that day. As for NewCases * 0.3. aawhile Italy had a admission rate of 50%, I estimated that the United States would have a lower number due to a younger population, although this number is offset slightly by the fact that America has higher rates of chronic conditions like cardiovascular disease and diabetes. In addition, across various news sources, especially for states that lack testing capabilities, only those who exhibit visible symptoms or were in direct contact with a coronavirus patient were tested, possibly eliminating asymptomatic patients who would otherwise not need to be hospitalized.

In terms of Deaths, I reached 0.8 based the followinng observations: On a single day New York added about 8220 additional deaths to their tally. NY Times says there were 3700 extra deaths reported that day from outside hospitals. This count includes an additional 600 deaths that would have occurred that during because of the coronavirus. Not taking into account those deaths, (3700-600)/118302 deaths or about 8.83% of deaths occurred outside of the hospital. Not every day would exhibit these numbers the additional 3022 deaths that were added to the tally included outside of hospital deaths for the previous day; in addition, numbers will vary from county to county, which is why I use a a more conservative number, resulting in 80% of reported deaths occurring within hospitals.
Also, since governor Cuomo said about 25% of positive cases need to be admitted to hospital and of those 25%, half need to be admitted to icu, I assume a death rate of 25% among those who enter the hospital. This would mean (1/3)*(0.25) = 8.33% of positive cases die, which is somewhat in line with the 11.25% reported by JHU in NYC if you take into account amount of deaths that occur outside of the hospital

As for discharges, I kept a separate dictionary of patients who enter the hospital each day. The median stay in hospital for discharged is 21 days. Every day we can assume that half of the newHospitalizaions from 21 days ago leave. Subtract the numbers left from the dictionary[index-21] tally and the total tally of people in hospital currently. This basic idea was used for an IQR of 15 days and 26 days to add accuracy to the model. I also subtracted deaths from the respective dictionary. Since median days from 1st symptoms to hospital admission = 7 days and median days from 1st symptoms to death = 14 days, median days from hospital admission to death = 7 days, so every day I subtracted the death tally from the dictionary value for 7 days ago. 

All code from above is available in HospBedsPrediction

Sources I used to arrive at my assumptions are:

https://www.statnews.com/2020/03/10/simple-math-alarming-answers-covid-19/

https://www.youtube.com/watch?v=DgQbRHaX3K4

https://www.nytimes.com/2020/04/14/nyregion/new-york-coronavirus-deaths.html

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7118526/

https://www.worldometers.info/coronavirus/coronavirus-death-rate/#hfr

**Webpage**
HTML, CSS, and Javascript code for my webpage are available under the webpage folder.
