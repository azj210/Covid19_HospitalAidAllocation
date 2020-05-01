ALTER TABLE t0 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t0; 

ALTER TABLE t1 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t1; 

ALTER TABLE t2 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t2; 

ALTER TABLE t3 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t3; 

ALTER TABLE t4 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t4; 

ALTER TABLE t5 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t5; 

ALTER TABLE t6 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t6; 

ALTER TABLE t7 SET TBLPROPERTIES('EXTERNAL'='False');
Drop table t7; 

CREATE EXTERNAL TABLE t0 (county string, state string, confirmedCases int, deaths int, deathRate float) row format delimited fields terminated by '!' location '/user/azj210/CovidD/output/';
CREATE EXTERNAL TABLE t1 (state string, county string, totalPop int, totalMale int) row format delimited fields terminated by '!' location '/user/azj210/Census/output/';
CREATE EXTERNAL TABLE t2 (city string, county string, state string, deviation float) row format delimited fields terminated by '!' location '/user/azj210/Hquality/output/';
CREATE EXTERNAL TABLE t3 (city string, state string, beds int) row format delimited fields terminated by '!' location '/user/azj210/Hbeds/output/';

CREATE EXTERNAL TABLE t4(county string, state string, beds int, deviation double);
INSERT INTO t4 SELECT t2.county, t2.state, t3.beds, t2.deviation FROM t2 JOIN t3 ON (t3.city = t2.city AND t3.state = t2.state);
CREATE EXTERNAL TABLE t5(county string, state string, beds bigint, deviation double);
INSERT INTO t5 SELECT t4.county, t4.state, SUM(t4.beds), AVG(t4.deviation) FROM t4 GROUP BY t4.county, t4.state ORDER BY t4.state, t4.county;


CREATE EXTERNAL TABLE t6(county string, state string, beds bigint, deviation double, totalPop int, totalMale int);
INSERT INTO t6 SELECT t5.county, t5.state, t5.beds, t5.deviation, t1.totalPop, t1.totalMale FROM t5 JOIN t1 ON t5.county = t1.county AND t5.state = t1.state;


CREATE EXTERNAL TABLE t7(county string, state string, beds bigint, deviation double, confirmedCases int, deaths int, deathRate double, totalPop int, totalMale int);
INSERT INTO t7 SELECT t6.county, t6.state, t6.beds, t6.deviation, t0.confirmedCases, t0.deaths, t0.deathRate, t6.totalPop, t6.totalMale FROM t6 JOIN t0 ON t6.county = t0.county AND t6.state = t0.state;
