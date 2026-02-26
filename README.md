# 🌍 Nonprofit Domain Intelligence Pipeline

A scalable data engineering pipeline designed to extract, classify, normalize, and maintain a continuously updated list of nonprofit organization domains from large-scale public web crawl datasets such as Common Crawl.

---

## 🚀 Project Objective

To simulate a production-scale web crawl indexing pipeline capable of:

- Processing Common Crawl WET files
- Extracting nonprofit candidate domains
- Detecting nonprofit content signals
- Normalizing root domains
- Deduplicating domain records
- Processing only new crawl releases (incremental ETL)
- Exporting structured nonprofit datasets
- Running scheduled automated pipeline execution

---

## 🏗️ Pipeline Workflow

Common Crawl periodically releases new crawl datasets identified by a crawl ID  
(e.g., CC-MAIN-2024-18).

Each crawl release is processed independently to extract nonprofit domains.

Pipeline Steps:

Common Crawl WET Data  
⬇  
Ingestion Layer  
⬇  
Domain Extraction  
⬇  
Nonprofit Keyword Detection  
⬇  
Root Domain Normalization  
⬇  
Deduplication  
⬇  
Crawl Tracker (checks if crawl already processed)  
⬇  
SQLite Storage  
⬇  
CSV Export  
⬇  
Scheduled Execution (Every 2 Hours)

The pipeline tracks previously processed crawl releases and processes only new crawl data instead of reprocessing the entire historical dataset.

This simulates incremental ETL pipelines commonly implemented in distributed environments such as:

- AWS EMR
- Apache Spark
- Databricks Delta Lake
- AWS Glue

---

## 🧰 Tech Stack Used

| Component | Technology |
|-----------|-------------|
Data Source | Common Crawl |
Processing | Python |
Domain Parsing | tldextract |
Storage | SQLite |
Scheduler | Linux Cron |
Reporting | CSV Export |
Environment | Python Virtual Environment |

---

## 🧠 Detection Signals (MVP)

The rule-based classification engine identifies nonprofit domains based on presence of:

- 501(c)(3)
- nonprofit
- charity
- donate
- foundation
- mission

Each detected signal contributes to a nonprofit score.

---

## 📊 Extracted Metadata

| Field | Description |
|--------|-------------|
root_domain | Canonical nonprofit domain |
nonprofit_score | Heuristic classification score |
signals | Detected nonprofit keywords |

---

## ⏰ Scheduled Pipeline Execution

Pipeline execution is automated using Linux Cron to simulate production scheduling:

0 */2 * * * run_pipeline.sh


Equivalent production tools include:

- AWS CloudWatch
- Apache Airflow
- n8n Workflow Automation

---

## 🧪 Development vs Production Implementation

This project is implemented using locally executed Python scripts on a sample subset of Common Crawl WET files for development and architectural validation purposes.

Due to the extremely large size of Common Crawl datasets (petabyte-scale), full production deployment of this pipeline would require distributed cloud infrastructure such as:

| Component | Production Service |
|-----------|--------------------|
Data Ingestion | AWS S3 |
Distributed Processing | AWS EMR (Spark) |
Orchestration | AWS Glue / Airflow |
Database | PostgreSQL / DynamoDB |
Scheduling | AWS CloudWatch |
Notification | AWS SES |

Only minimal configuration changes would be required to transition from local execution to production-scale distributed deployment.

---

## 📦 Output

The final output is exported as:

Equivalent production tools include:

- AWS CloudWatch
- Apache Airflow
- n8n Workflow Automation

---

## 🧪 Development vs Production Implementation

This project is implemented using locally executed Python scripts on a sample subset of Common Crawl WET files for development and architectural validation purposes.

Due to the extremely large size of Common Crawl datasets (petabyte-scale), full production deployment of this pipeline would require distributed cloud infrastructure such as:

| Component | Production Service |
|-----------|--------------------|
Data Ingestion | AWS S3 |
Distributed Processing | AWS EMR (Spark) |
Orchestration | AWS Glue / Airflow |
Database | PostgreSQL / DynamoDB |
Scheduling | AWS CloudWatch |
Notification | AWS SES |

Only minimal configuration changes would be required to transition from local execution to production-scale distributed deployment.

---

## 📦 Output

The final output is exported as:

output/nonprofit_domains.csv

Containing deduplicated nonprofit candidate domains with scoring metadata.

---

## 📈 Future Enhancements

- ML-based nonprofit classification
- Domain enrichment APIs
- REST API layer for SaaS deployment
- Cloud-native EMR Spark implementation

---

## 👨‍💻 Author

Bala Venkatesh  
AWS Data Engineer  
Python | Spark | AWS | Data Engineering
