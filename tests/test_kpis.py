from pyspark.sql import SparkSession
from src.data_processing import clean_salary_columns

spark = SparkSession.builder \
    .appName("test") \
    .getOrCreate()

def test_avg_salary():
    df = spark.createDataFrame(
        [(50000, 70000)],
        ["Salary Range From", "Salary Range To"]
    )

    result = clean_salary_columns(df)
    assert result.collect()[0]["avg_salary"] == 60000