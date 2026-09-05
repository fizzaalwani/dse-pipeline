# Dhaka Stock Exchange Data Engineering Pipeline

A Dockerized data engineering pipeline that extracts, processes, stores, and compares financial and corporate data from the **Dhaka Stock Exchange (DSE)**.

The project automates the collection of DSE company information and organizes the resulting datasets into date-based folders, making it possible to track changes in company, market, financial, dividend, shareholder, and corporate information over time.

---

## 🚀 Project Overview

Financial market websites contain large amounts of information that is difficult to monitor manually.

This project was built to automate that process.

The pipeline:

1. Connects to the DSE website
2. Extracts data for listed companies
3. Processes and structures the scraped information
4. Stores datasets as CSV files
5. Organizes data by extraction date
6. Maintains pipeline logs
7. Compares datasets between different dates
8. Detects changes in company and financial records
9. Runs inside a Docker container
10. Uses Docker Compose for reproducible execution

The pipeline currently handles data for **600+ companies** listed on the DSE.

---

# 🏗️ Architecture

```text
                    Dhaka Stock Exchange
                             │
                             ▼
                    ┌─────────────────┐
                    │   Data Scraping │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Data Extraction │
                    │  & Processing   │
                    └────────┬────────┘
                             │
                             ▼
                 ┌─────────────────────────┐
                 │ Date-Based Data Storage │
                 │                         │
                 │ processed_data/         │
                 │   YYYY-MM-DD/           │
                 │      *.csv              │
                 └───────────┬─────────────┘
                             │
                             ▼
                 ┌─────────────────────────┐
                 │    Change Detection     │
                 │ Previous vs Current     │
                 │       Dataset           │
                 └───────────┬─────────────┘
                             │
                             ▼
                 ┌─────────────────────────┐
                 │       CSV Output        │
                 │ + Pipeline Logs         │
                 └─────────────────────────┘

                         Docker
                    ┌─────────────┐
                    │ DSE Pipeline│
                    └─────────────┘
                         │
                    Docker Compose
```

---

# 📂 Project Structure

```text
Dhaka Stock Exchange/
│
├── scraping.ipynb
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── processed_data/
│   ├── 2026-09-05/
│   │   ├── companies.csv
│   │   ├── market_info.csv
│   │   ├── basic_info.csv
│   │   ├── agm_info.csv
│   │   ├── cash_dividend.csv
│   │   ├── bonus_issues.csv
│   │   ├── price_earnings.csv
│   │   ├── listing_info.csv
│   │   ├── shareholder_history.csv
│   │   ├── company_secretaries.csv
│   │   ├── corporate_status.csv
│   │   ├── financial_performance.csv
│   │   └── interim_financial_performance.csv
│   │
│   └── YYYY-MM-DD/
│
└── logs/
    └── pipeline_YYYY-M-D.log
```

---

# 📊 Data Collected

The pipeline extracts multiple categories of DSE information.

### Company Information

* Company names
* Trading codes
* Company details
* Basic company information

### Market Information

* Market-related information
* Price and market metrics

### Corporate Information

* AGM information
* Company secretaries
* Listing information
* Corporate status

### Financial Information

* Financial performance
* Interim financial performance
* Price/Earnings information

### Investor Information

* Shareholder history
* Shareholder categories

### Dividend Information

* Cash dividends
* Bonus issues

This separates the scraped information into logical datasets instead of maintaining one large unstructured file.

---

# 🔄 Data Extraction Pipeline

The pipeline starts by requesting data from the DSE website.

The scraper first obtains the list of companies and then processes the available company information.

The extracted data is separated into individual datasets such as:

```text
companies
market_info
basic_info
agm_info
cash_dividend
bonus_issues
price_earnings
listing_info
shareholder_history
company_secretaries
corporate_status
financial_performance
interim_financial_performance
```

The pipeline successfully handles **636 companies** in the current extraction.

---

# 📅 Date-Based Data Storage

Instead of overwriting the previous dataset, each extraction is stored under its corresponding date.

For example:

```text
processed_data/
│
├── 2026-09-04/
│   ├── companies.csv
│   ├── market_info.csv
│   └── ...
│
└── 2026-09-05/
    ├── companies.csv
    ├── market_info.csv
    └── ...
```



# 📝 Logging

The pipeline implements logging to monitor the scraping and processing process.

Logs contain information such as:

* Request status
* Scraping progress
* Number of companies scraped
* Download progress
* Extraction status
* Output files
* Errors and warnings

Example:

```text
Request successful
Scraped 636 companies
Download completed
Extraction completed
Saved companies.csv
Saved market_info.csv
...
```

Logs are stored separately from the processed datasets:

```text
logs/
└── pipeline_2026-9-5.log
```

This makes debugging and monitoring easier.

---

# 🐳 Dockerization

The entire pipeline is containerized using Docker.

Instead of depending on the developer's local Python environment, the project packages its runtime environment into a Docker image.

The Docker image contains:

* Python
* Required dependencies
* Project source code
* Jupyter/Notebook execution environment
* Pipeline configuration

The notebook can then be executed inside the container.

---

# 🐳 Dockerfile

The Dockerfile defines how the pipeline environment is built.

Conceptually:

```text
Python Base Image
       │
       ▼
Install Dependencies
       │
       ▼
Copy Project Files
       │
       ▼
Set Working Directory
       │
       ▼
Execute scraping.ipynb
```

This makes the pipeline reproducible across different machines.

---

# ⚙️ Docker Compose

Docker Compose is used to define how the DSE pipeline container should run.

A key part of the configuration is the volume mapping:

```yaml
volumes:
  - ./processed_data:/app/processed_data
  - ./logs:/app/logs
```

This connects the Docker container to folders on the local machine.

Therefore:

```text
Container
/app/processed_data
        │
        ▼
Local Machine
./processed_data
```

and:

```text
Container
/app/logs
        │
        ▼
Local Machine
./logs
```

This means generated data and logs remain available even after the container stops.

---

# ▶️ Running the Pipeline

Make sure Docker Desktop is running.

Navigate to the project directory:

```bash
cd "C:\Users\fizza\OneDrive\Documents\internship\Dhaka Stock Exchange"
```

Build and start the pipeline:

```bash
docker compose up --build
```

The `--build` flag ensures that the Docker image is rebuilt when project files or dependencies have changed.

For subsequent runs where nothing changed:

```bash
docker compose up
```

To run in the background:

```bash
docker compose up -d --build
```

---

# 📋 Monitoring the Pipeline

View Docker logs:

```bash
docker compose logs -f dse-pipeline
```

The scraping application also writes detailed logs to:

```text
logs/
```

On Windows PowerShell:

```powershell
Get-Content .\logs\pipeline_2026-9-5.log -Wait
```

---

# 🛑 Stopping the Pipeline

To stop the running pipeline:

```bash
docker compose down
```

The Docker container and network are removed, while the locally mounted:

```text
processed_data/
logs/
```

remain on the machine.

---

# 💾 Data Persistence

Data persistence is handled using Docker bind mounts.

Without a volume:

```text
Container
   │
   └── processed_data
          │
          └── Data can disappear when container is removed
```

With the configured volume:

```text
Container                    Local Machine

/app/processed_data  ──────► ./processed_data
/app/logs            ──────► ./logs
```

This ensures that the output of the pipeline is accessible outside Docker.

---

# 🛠️ Technologies Used

| Technology                   | Purpose                            |
| ---------------------------- | ---------------------------------- |
| Python                       | Data extraction and processing     |
| Pandas                       | Data manipulation and comparison   |
| Jupyter Notebook             | Pipeline development and execution |
| Docker                       | Containerization                   |
| Docker Compose               | Container orchestration            |
| CSV                          | Structured data storage            |
| Logging                      | Pipeline monitoring and debugging  |
| HTTP Requests / Web Scraping | DSE data extraction                |

---

# 🔧 Data Engineering Concepts Implemented

This project demonstrates several practical data engineering concepts:

* Data extraction
* Web scraping
* Data processing
* Data transformation
* Structured data storage
* Historical snapshots
* Business keys
* Record comparison
* Change detection
* Data versioning
* Pipeline logging
* Containerization
* Reproducible environments
* Docker volumes
* Docker Compose
* Automated notebook execution

---

# 📈 Future Improvements

The current pipeline provides the foundation for a larger production-grade data platform.

Possible improvements include:

### 1. Data Warehouse

Load the processed data into a relational or analytical warehouse such as:

```text
PostgreSQL
      ↓
Data Warehouse
      ↓
BI Dashboard
```

### 2. Medallion Architecture

The pipeline could be expanded into:

```text
Bronze
  ↓
Raw scraped data

Silver
  ↓
Cleaned and transformed data

Gold
  ↓
Analytics-ready datasets
```

### 3. Slowly Changing Dimensions

The current date-based snapshots and change detection can be extended into:

```text
Dimension Tables
      │
      ├── effective_from
      ├── effective_to
      └── is_current
```

allowing historical company information to be tracked.

### 4. Apache Airflow

The pipeline can be scheduled using Airflow:

```text
Airflow
   │
   ▼
Daily Scraping
   │
   ▼
Data Processing
   │
   ▼
Change Detection
   │
   ▼
Warehouse
   │
   ▼
BI Dashboard
```

### 5. Automated Data Quality Checks

Future versions can include checks for:

* Missing values
* Duplicate records
* Unexpected row counts
* Invalid trading codes
* Schema changes
* Failed downloads

### 6. BI Dashboard

The final data can be connected to a BI tool to provide analytics such as:

* Company performance
* Market trends
* Dividend history
* Financial performance
* Shareholder changes
* Company listings
* Historical changes

---

# 🎯 Project Outcome

This project transforms manually collected DSE information into a repeatable and containerized data pipeline.

Instead of:

```text
Website
   ↓
Manual Download
   ↓
Excel/CSV
   ↓
Manual Comparison
```

the system moves toward:

```text
DSE
 │
 ▼
Automated Extraction
 │
 ▼
Data Processing
 │
 ▼
Date-Based Storage
 │
 ▼
Change Detection
 │
 ▼
Historical Data
 │
 ▼
Analytics / Data Warehouse
```

The project demonstrates how a web-based source can be transformed into a structured, reproducible **data engineering workflow** with historical tracking and containerized execution.
