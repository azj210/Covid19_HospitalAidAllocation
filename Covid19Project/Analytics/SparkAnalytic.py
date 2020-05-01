from pyspark import SparkContext
from pyspark.sql import HiveContext

#create dataframe for beds predicitons
beds = sqlContext.read.json("/user/azj210/BedsNeeded.json")
beds.registerTempTable("bedsNeeded")
table = sqlContext.sql("select * from bedsNeeded")
table.show()
table.collect()

#get table from hive 
hc = HiveContext(sc)
hiveTable= hc.sql("select county, state, beds from azj210.t7")


#joined tables
#alphabetical arragement
joined = hiveTable.join(table, on=["county", "state"], how='inner')
joined.write.saveAsTable("azj210.430predicts")













