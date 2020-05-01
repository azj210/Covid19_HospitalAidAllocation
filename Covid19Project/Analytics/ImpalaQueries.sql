invalidate metadata azj210.t7;

ALTER TABLE cor1 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor1; 

ALTER TABLE cor2 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor2; 

ALTER TABLE cor3 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor3; 

ALTER TABLE cor4 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor4; 

ALTER TABLE cor5 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor5; 

ALTER TABLE cor6 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor6; 

ALTER TABLE cor7 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor7; 

ALTER TABLE cor8 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table cor8; 


SELECT (((COUNT(deathRate) * SUM(deathRate * deviation)) - (SUM(deathRate) * SUM(deviation))) / (SQRT((COUNT(deviation) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(deathRate) * SUM(deviation * deviation)) - (SUM(deviation) * SUM(deviation))))) AS "Correlation" FROM t7;

SELECT (((COUNT(deathRate) * SUM(deathRate * beds)) - (SUM(deathRate) * SUM(beds))) / (SQRT((COUNT(deathRate) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(deathRate) * SUM(beds * beds)) - (SUM(beds) * SUM(beds))))) AS "Correlation" FROM t7;

SELECT (((COUNT(deaths) * SUM(deaths * beds)) - (SUM(deaths) * SUM(beds))) / (SQRT((COUNT(deaths) * SUM(deaths * deaths)) - (SUM(deaths) * SUM(deaths))) * SQRT((COUNT(deaths) * SUM(beds * beds)) - (SUM(beds) * SUM(beds))))) AS "Correlation" FROM t7;

SELECT (((COUNT(deathRate) * SUM(deathRate * totalpop)) - (SUM(deathRate) * SUM(totalpop))) / (SQRT((COUNT(deathRate) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(deathRate) * SUM(totalpop * totalpop)) - (SUM(totalpop) * SUM(totalpop))))) AS "Correlation" FROM t7;

SELECT (((COUNT(deathRate) * SUM(deathRate * totalmale)) - (SUM(deathRate) * SUM(totalmale))) / (SQRT((COUNT(deathRate) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(deathRate) * SUM(totalmale * totalmale)) - (SUM(totalmale) * SUM(totalmale))))) AS "Correlation" FROM t7;


SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM t7;

CREATE EXTERNAL TABLE cor1(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor1 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >= 100;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor1;

CREATE EXTERNAL TABLE cor2(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor2 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >= 200;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor2;

CREATE EXTERNAL TABLE cor3(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor3 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >=400;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor3;

CREATE EXTERNAL TABLE cor4(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor4 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >=800;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor4;

CREATE EXTERNAL TABLE cor5(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor5 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >=1400;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor5;

CREATE EXTERNAL TABLE cor6(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor6 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >=2400;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor6;

CREATE EXTERNAL TABLE cor7(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor7 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >=6000;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor7;

CREATE EXTERNAL TABLE cor8(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO cor8 SELECT t7.county, t7.state, t7.beds, t7.deviation, t7.confirmedCases, t7.deaths, t7.deathRate, t7.totalPop, t7.totalMale FROM t7 WHERE confirmedCases >=10000;
SELECT (((COUNT(confirmedcases) * SUM(deathRate * confirmedcases)) - (SUM(deathRate) * SUM(confirmedcases))) / (SQRT((COUNT(confirmedcases) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(confirmedcases) * SUM(confirmedcases * confirmedcases)) - (SUM(confirmedcases) * SUM(confirmedcases))))) AS "Correlation" FROM cor8;


--between deathRate and (confirmedcases/elderlypop) -> assuming most of the confirmedCases are hospitalized individuals that reflect more on the elderly population, this number would be closer to percent of elderly infected
CREATE EXTERNAL TABLE c2(county string, state string, deathRate double, confirmedCases int, totalPop int, toCalc double);
INSERT INTO c2 SELECT t7.county, t7.state, t7.deathRate, t7.confirmedCases, t7.totalPop, (t7.confirmedCases/t7.totalPop) FROM t7;
SELECT (((COUNT(deathRate) * SUM(deathRate * toCalc)) - (SUM(deathRate) * SUM(toCalc))) / (SQRT((COUNT(deathRate) * SUM(deathRate * deathRate)) - (SUM(deathRate) * SUM(deathRate))) * SQRT((COUNT(deathRate) * SUM(toCalc * toCalc)) - (SUM(toCalc) * SUM(toCalc))))) AS "Correlation" FROM c2;


-- counties with deathrate higher than national avg and confirmedCases > 10
SELECT * FROM t7 WHERE deathRate > (SELECT AVG(deathRate) FROM t7) AND confirmedCases < 10 ORDER BY deathRate DESC;
/* conclusion from the above. It appears as though there isn't much correlation between deathrate and factors like number of elderly, quality of hospital care in the county, and hospital beds in the county
rather it seems as though deathrate would be more correlated to factors like wherever there is a higher coronavirus outbreak. 
Ironically even factors like elderly population to number of deaths(not death rate) doesn't even yield a significant correlation value.
I think that this just shows proves that the coronavirus isn't necessarily a very deadly illness. There are many factors that contribute to its spread
and severity, but it seems as though the 
*/

--counties where elderly male > 50% of population
SELECT * FROM t7 WHERE (totalmale/totalpop > 0.50);
-- 19/1371 counties. The vast majority of counties have more elderly female

--counties where hospital beds < national avg and cases > national avg and deathrate > national avg aka hardest hit counties
--**use this
CREATE EXTERNAL TABLE at1(county string, state string, beds bigint, deviation double, confirmedcases int, deaths int, deathrate double, totalpop int, totalmale int);
INSERT INTO at1 SELECT * FROM t7 WHERE beds < (SELECT AVG(beds) FROM t7) AND confirmedcases > (SELECT AVG(confirmedcases) from t7) AND deathrate > (SELECT AVG (deathrate) from t7);
--8/1369

