✅ Project Summary



This project performs an end-to-end analysis of the NYC jobs dataset using PySpark to derive key workforce insights. The dataset contains job postings from the City of New York official job board including job metadata, salary ranges, qualifications, and agency information. The pipeline is modular and designed for processing, feature engineering, KPI computation, visualization, and documentation.



📊 Data Exploration



The source dataset was explored to understand column types (numerical, categorical, text, dates), missing values, and basic distributions.



Key observations:



Numerical Columns: Salary Range From, Salary Range To



Categorical Columns: Agency, Job Category, Posting Type



Text Columns: Job Description, Minimum Qualifications



Date Columns: Posting Date



Missing values were handled appropriately, and text fields were cleaned using standardization (lowercasing, trimming). Outliers in salary values were identified and analyzed.



📈 Key KPIs and Results



Top 10 Job Categories



Computed using grouping and ordered by posting count.



Results were visualized using Seaborn bar chart.



Salary Distribution per Job Category



Average salaries computed by midpoint of salary range.



Distribution for top categories visualized using boxplots.



Histogram of overall salary distribution also generated.



Correlation between Higher Degree Requirement \& Salary



Created a binary feature representing presence of a degree in qualification text.



Correlation between degree requirement and salary was computed and interpreted.



Highest Salary per Agency



For each agency, the job posting with the highest average salary was identified.



Average Salary per Agency (Last 2 Years)



Date logic was applied to restrict data to 2 years.



Average salaries computed and visualized.



Highest Paid Skills



Text analysis on job descriptions for selected skills (Python, SQL, Spark, AWS).



Average salary by skill group identified and visualized.



🛠 Data Processing and Feature Engineering



A set of reusable PySpark functions were developed to perform:



Null handling (handle\_null\_values)



Salary midpoint calculation (clean\_salary\_columns)



Text normalization



Binary feature flag creation (degree, skills)



Experience extraction using regex



Categorical encoding where relevant



Feature engineering techniques applied:



Salary Midpoint Calculation



Degree Requirement Binary Flag



Experience Years Extraction



Skill Flags as binary features



Features deemed irrelevant (too many missing values or redundant) were dropped based on profiling.



📊 Visualization Summary



Visualizations were generated in the notebook using:



Matplotlib



Seaborn



Examples include:



Bar chart for top job categories



Boxplot for salary distributions



Histogram of salary ranges



Scatter plot for degree vs salary



Visuals were limited to top categories to maintain clarity and readability.



⚙ Code Testing



Unit tests were developed for:



Salary midpoint function



Feature flag extraction



Degree and skill feature tests



Testing was done using pytest and verified expected outputs against known inputs.



🧪 Deployment Proposal



Two deployment strategies are proposed:



Airflow Pipeline



Automated orchestration



Scheduled daily ingestion



DAG triggers for ETL tasks



Dockerized Spark Job



Multi-container architecture



Spark master + workers



Automated spark-submit via entrypoint



Deployment would target cloud via AWS EMR or Databricks.



📌 Execution Triggers



Scheduled daily runs via CRON



Event-based trigger on new data landing in S3



Versioning and monitoring via Airflow



🧠 Learnings \& Challenges



Handling inconsistent salary formats (hourly vs yearly)



Managing lazy evaluation in Spark



Efficient conversion from Spark to Pandas for visualization



Ensuring the flexibility of feature engineering pipeline



Balancing code readability with performance



🔍 Assumptions



Salary midpoint reasonably approximates actual compensation



Keyword based skill extraction assumes specific terminology



Correlation is interpreted at aggregate level with simple Pearson correlation in PySpark

