from pyspark.sql.functions import when, col, regexp_extract, lower

def add_degree_flag(df):
    return df.withColumn(
        "requires_degree",
        when(lower(col("Minimum Qual Requirements")).contains("degree"), 1).otherwise(0)
    )

def extract_experience_years(df):
    return df.withColumn(
        "experience_years",
        regexp_extract(col("Minimum Qual Requirements"), r'(\d+) year', 1)
    )

def add_skill_flags(df, skills):
    for skill in skills:
        df = df.withColumn(
            skill,
            when(lower(col("Job Description")).contains(skill), 1).otherwise(0)
        )
    return df