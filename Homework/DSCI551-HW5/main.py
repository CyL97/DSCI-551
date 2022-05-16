import pyspark.sql.functions as fc
from pyspark.sql import SparkSession

def splitFunca(row):
    row_list = row.split(',')
    if row_list[1] == 'Male' and row_list[-1] == 'Yes':
        return True

def splitFuncb(row):
    row_list = row.split(',')
    if row_list[-1] == 'Yes':
        if row_list[-2] == ' ':
            row_list[-2] = '0'
        return (row_list[1], float(row_list[-2]))

if __name__ == '__main__':
    spark = SparkSession.builder.enableHiveSupport().getOrCreate()
    churn = spark.read.options(header='True', inferSchema='True', delimiter=',').csv("churn.csv")
    churn = churn.withColumn('TotalCharges', fc.col('TotalCharges').cast('double'))
    print(churn)
    #churn.show()
    #Qa_show = churn.filter((churn['gender'] == 'Male') & (churn['Churn'] == 'Yes')).show()
    Qa = churn.filter((churn['gender'] == 'Male') & (churn['Churn'] == 'Yes')).count()
    print(Qa)
    Qb = churn.filter(churn['Churn'] == 'Yes').groupBy('gender').agg(fc.max('TotalCharges'))
    Qb.show()
    Qc = churn.filter(churn['Churn'] == 'Yes').groupBy('gender').count()
    Qc.show()
    Qd = churn.groupBy(['churn', 'contract']) \
        .count() \
        .withColumnRenamed("count", "cnt") \
        .orderBy('churn', fc.desc('cnt'))
    Qd.show()
    Qe = churn.groupBy(['gender', 'churn']) \
        .count() \
        .where(fc.col('count') > 1000)
    Qe.show()

    lines = spark.sparkContext.textFile("churn.csv")

    Qa_RDD = lines.map(splitFunca).filter(lambda row: row is not None).count()
    print("RDD_Qa: ",Qa_RDD)

    Qb_RDD = lines.map(splitFuncb).filter(lambda row: row is not None).groupByKey().map(lambda x:(x[0], max(x[1]))).collect()
    print("RDD_Qb: ",Qb_RDD)

