from pyspark.sql.functions import avg, max

def top_10_job_categories(df):
    return df.groupBy("Job Category") \
             .count() \
             .orderBy("count", ascending=False) \
             .limit(10)

def salary_distribution_per_category(df):
    return df.groupBy("Job Category") \
             .avg("avg_salary")

def highest_salary_per_agency(df):
    return df.groupBy("Agency") \
             .agg(max("avg_salary").alias("max_salary"))

def avg_salary_last_2_years(df):
    return df.groupBy("Agency") \
             .avg("avg_salary")