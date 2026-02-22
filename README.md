📊 NYC Jobs Data Engineering Assessment
📌 Project Overview

This project performs an end-to-end analysis of NYC job postings using PySpark.
The objective is to demonstrate data engineering best practices including:

Data exploration and profiling

Data cleaning and transformation

Feature engineering

KPI computation

Visualization

Modular pipeline design

Test coverage

Deployment strategy proposal

The dataset contains job postings from the official New York City Jobs portal, including internal and external postings.

🏗 Project Architecture
nyc-jobs-data-engineering/
│
├── data/                   # Raw dataset (nyc-jobs.csv)
├── notebooks/              # Exploratory analysis & visualizations
├── src/                    # Modular PySpark business logic
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── kpi_analysis.py
│   └── utils.py
├── tests/                  # Unit tests
├── output/                 # Processed dataset (Parquet format)
├── main.py                 # Production pipeline entry point
├── MyDocument.md           # Detailed documentation
├── requirements.txt
└── docker-compose.yml

🧰 Tech Stack

Python 3.x

PySpark

Pandas

Matplotlib

Seaborn

Pytest

Docker (optional deployment)

📂 Dataset

Source: NYC official job postings
Format: CSV
Contains:

Job metadata

Agency information

Salary ranges

Qualification requirements

Posting dates

Job descriptions

🔍 Data Exploration

The dataset was analyzed to identify:

Numerical columns (Salary Range From, Salary Range To)

Categorical columns (Agency, Job Category, Posting Type)

Text fields (Job Description, Minimum Qualifications)

Missing values and inconsistencies

🛠 Data Processing

The following transformations were applied:

Null handling

Salary midpoint calculation

Text normalization

Date conversion

Column pruning based on profiling

Processed dataset is stored in Parquet format for optimized querying.

🧠 Feature Engineering

Implemented feature engineering techniques:

Salary midpoint (avg_salary)

Degree requirement binary flag

Experience extraction using regex

Skill-based binary encoding (Python, SQL, AWS, Spark)

📊 KPIs Computed

Top 10 job categories by number of postings

Salary distribution per job category

Correlation between degree requirement and salary

Highest salary per agency

Average salary per agency (last 2 years)

Highest paid skills in the US market

Visualizations were generated using Seaborn and Matplotlib.

🚀 How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Run Using Notebook (Recommended for Analysis)
jupyter notebook
Open:
notebooks/assessment_notebook.ipynb
3️⃣ Run Production Pipeline
spark-submit main.py
📈 Spark UI Monitoring

While running:
http://localhost:4040
If unavailable, check:
http://localhost:4041
🧪 Running Tests
pytest tests/
🐳 Docker Deployment (Optional)

To run using Docker:
docker-compose up --build
This sets up Spark master and worker nodes for distributed execution.

⚙ Deployment Strategy

Proposed deployment approaches:

Apache Airflow for orchestration

AWS EMR / Databricks for scalable execution

S3 Data Lake for storage

Dashboard integration (Power BI / Tableau)

📌 Key Learnings

Importance of modular PySpark design

Handling Spark lazy evaluation

Efficient aggregation before visualization

Avoiding large .toPandas() conversions

Managing distributed computation

📎 Author

Madhu Mitha
Data Engineering Candidate