# main.py

from pyspark.sql import SparkSession
from sys import path
from time import time

path.insert(0, "/app")


def readjob(spark: SparkSession, **kwargs):
    """
    readjob

    Alternative job that reads from the database into a DataFrame

    The table is initially empty but you can use this to verify the
    main job did what it was supposed to.

    INPUTS:
        spark - active SparkSession
        **kwargs - keyword arguments from spark-submit    

    """

    jdbc_url = "jdbc:postgresql://database:5432/sparxcercise"

    df = (
        spark
            .read
            .format("jdbc")
            .option("url", jdbc_url)
            .option("user", "postgres")
            .option("password", "postgres")
            .option("driver", "org.postgresql.Driver")
            .option("dbtable", "medals")
            .load()
    )

    df.show()


def myjob(spark: SparkSession, **kwargs):
    """
    myjob
    
    Main entrypoint for PySpark job

    INPUTS:
        spark - active SparkSession
        **kwargs - keyword arguments from spark-submit

    """
    df = spark.read.csv("spark-data/Medals.csv")

    jdbc_url = "jdbc:postgresql://database:5432/sparxcercise"

    conn_properties = {"user": "postgres", "password": "postgres", "driver": "org.postgresql.Driver"}

    df.write.jdbc(jdbc_url, table="medals", mode="overwrite", properties=conn_properties)


if __name__ == "__main__":

    spark = (
        SparkSession
            .builder
            .config("spark.jars.packages", "org.postgresql:postgresql:42.2.20")
            .appName("exercise")
            .master("spark://spark-master:7077")
            .getOrCreate()
    )

    start = time()
    myjob(spark)
    end = time()

    print(f"\nExecution of job took {end-start:.8f} seconds\n")
