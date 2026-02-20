from pyspark.sql.functions import col, when, trim, lower

def clean_salary_columns(df):
    return df.withColumn(
        "avg_salary",
        (col("Salary Range From") + col("Salary Range To")) / 2
    )

def handle_null_values(df):
    return df.fillna({
        "Salary Range From": 0,
        "Salary Range To": 0
    })

def standardize_text_columns(df, column):
    return df.withColumn(column, lower(trim(col(column))))

def remove_unnecessary_columns(df):
    drop_cols = ["Recruitment Contact", "Additional Information"]
    return df.drop(*drop_cols)