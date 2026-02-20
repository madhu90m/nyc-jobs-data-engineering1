from pyspark.sql import SparkSession
from src.data_processing import *
from src.feature_engineering import *

def run_pipeline():
    spark = SparkSession.builder.appName("NYC Jobs").getOrCreate()
    df = spark.read.csv("data/nyc-jobs.csv", header=True, inferSchema=True)

    df = handle_null_values(df)
    df = clean_salary_columns(df)

    df.write.mode("overwrite").parquet("output/processed_nyc_jobs.parquet")

if __name__ == "__main__":
    run_pipeline()

import time
time.sleep(60)