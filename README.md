# 🌍 B2B Trade Intelligence Pipeline

An end-to-end Data Engineering project that builds a real-world B2B trade intelligence platform using global import/export trade data from the UN Comtrade API.

The system automatically collects, cleans, stores, serves, and visualizes international trade data so businesses can analyze trade flows, identify major trading partners, monitor product-level trends, and make data-driven decisions.

This project was built as part of a Data Engineering assignment focused on designing a dynamic, production-style B2B data pipeline.

---

# 📌 Assignment Objective

The assignment required building a complete end-to-end B2B data pipeline that:

* Solves a real business problem using data
* Automates data collection and cleaning
* Stores data in a reliable database
* Exposes a usable endpoint or interface
* Deploys the solution in a reproducible way
* Demonstrates engineering thinking, reliability, and scalability

This project addresses all three required phases:

* Scraping
* Cleaning & Automation
* Deployment

---

# 🧩 B2B Problem Being Solved

Businesses involved in international trade often struggle to access structured and actionable trade intelligence data.

Raw trade datasets are:

* Massive
* Inconsistent
* Difficult to query
* Not business-user friendly
* Hard to automate and visualize

Companies frequently need answers to questions like:

* Which countries are importing/exporting specific products?
* Which trading partners are growing over time?
* What products have the highest trade value?
* Which markets are emerging opportunities?
* How do trade flows change yearly?

Manually analyzing raw datasets or API responses is inefficient and time-consuming.

This project solves that problem by building a centralized trade intelligence pipeline that continuously collects and processes trade data into business-friendly APIs and dashboards.

---

# 💼 Business Value

The platform enables businesses to:

## 📈 Analyze Import/Export Trends

The system stores historical trade records in PostgreSQL, enabling long-term trade analysis.

Businesses can:

* Track trade growth over time
* Compare yearly trade values
* Identify market expansion opportunities
* Detect declining trade regions

Example:
An electronics exporter can analyze how laptop exports from China changed across different countries over multiple years.

---

## 🌍 Identify Major Trading Partners

The dashboard and APIs help businesses discover the most significant import/export partners for a country or product category.

This helps organizations:

* Understand dependency on certain markets
* Optimize supply chain decisions
* Explore international expansion
* Identify high-value trade relationships

---

## 📦 Monitor Product-Level Trade Flows

Trade data is categorized using HS product codes.

Businesses can:

* Track product-specific demand
* Compare import vs export performance
* Analyze trade quantity and weight
* Monitor product-level market shifts

This is useful for:

* Manufacturers
* Exporters
* Importers
* Supply chain teams
* Market analysts

---

## 📊 Access Interactive Trade Intelligence Dashboards

Instead of analyzing raw CSV files manually, businesses receive:

* KPI metrics
* Interactive charts
* Filterable dashboards
* Country-level insights
* Product-level analytics

This improves:

* Decision-making speed
* Data accessibility
* Business intelligence capabilities

---

# ⚙️ Why This Project Is Useful

This project demonstrates how real-world ETL systems work in production.

The pipeline:

* Continuously ingests external data
* Cleans and standardizes records
* Stores structured data in PostgreSQL
* Exposes analytics APIs using FastAPI
* Visualizes insights using Streamlit
* Automates updates using APScheduler
* Uses Docker for reproducible deployment

The solution is dynamic, not static:

* Data changes over time
* Pipeline can rerun automatically
* Database updates continuously
* APIs and dashboard reflect latest data

---

# 🏗️ System Architecture

```text
UN Comtrade API
        ↓
Scraper
        ↓
Cleaner
        ↓
PostgreSQL
        ↓
FastAPI APIs
        ↓
Streamlit Dashboard
```

---

# 🛠️ Tech Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Language         | Python 3.12             |
| Database         | PostgreSQL 16           |
| Backend API      | FastAPI                 |
| ORM              | SQLAlchemy              |
| Dashboard        | Streamlit               |
| Data Processing  | pandas                  |
| Scheduling       | APScheduler             |
| Containerization | Docker + Docker Compose |

---

# 📂 Project Structure

```bash
zauba-trade-intelligence/
│
├── scraper/
│   ├── scraper.py
│   └── utils.py
│
├── cleaning/
│   ├── cleaner.py
│   └── decisions.md
│
├── pipeline/
│   ├── load_to_db.py
│   └── scheduler.py
│
├── api/
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── data/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Phase 1 — Scraper

## ✅ Objective

Build a reliable scraper for a real B2B dataset.

## ✅ Data Source

UN Comtrade Public API:

* Global import/export trade data
* Country-level trade intelligence
* Product-level trade statistics

## ✅ Features Implemented

### Pagination Handling

The scraper supports paginated API responses to fetch large datasets reliably.

### Missing Field Handling

Missing values are safely handled using defensive parsing logic.

### Failure & Retry Handling

The scraper includes retry-safe request handling to avoid hard crashes.

### Structured Raw Data Export

Raw data is exported into:

* JSON
* CSV

---

# Phase 2 — Cleaning & Automation

## ✅ Data Cleaning

Raw trade datasets are inconsistent and contain duplicates.

Cleaning pipeline performs:

* Duplicate removal
* Missing value handling
* Data standardization
* Timestamp normalization
* Type conversion

All cleaning decisions are documented in:

```text
cleaning/decisions.md
```

---

## ✅ Database Storage

Cleaned records are stored in PostgreSQL using SQLAlchemy ORM.

Benefits:

* Structured querying
* Scalable storage
* Efficient filtering
* API integration

---

## ✅ Automation

Pipeline automation implemented using APScheduler.

Automated workflow:

1. Run scraper
2. Clean raw data
3. Load into PostgreSQL
4. Update APIs/dashboard automatically

Schedule:

* Runs daily at 2 AM

This ensures:

* Data stays updated
* Pipeline runs without manual intervention
* Outputs remain reliable and repeatable

---

# Phase 3 — Deployment

## ✅ Deployment Objective

Expose a real interface/API that a business user can interact with.

This project provides:

* FastAPI analytics endpoints
* Streamlit dashboard interface
* Dockerized deployment setup

---

# 🔌 API Endpoints

## Health Check

```http
GET /health
```

## Get All Trade Records

```http
GET /trades
```

## Filter Trade Records

```http
GET /trades/filter
```

### Supported Query Parameters

| Parameter | Example   |
| --------- | --------- |
| year      | 2014      |
| reporter  | China     |
| partner   | India     |
| product   | Computers |
| flow      | Export    |

---

# 📊 Dashboard Features

The Streamlit dashboard provides:

* Year filtering
* Country filtering
* Flow-type filtering
* KPI metrics
* Top products visualization
* Top trading partners
* Interactive charts
* Live PostgreSQL integration

---

# 🐳 Dockerized Deployment

The project supports one-command local deployment using Docker Compose.

## Start Entire Platform

```bash
docker compose up --build
```

This starts:

* PostgreSQL
* FastAPI
* Streamlit

---

# ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://postgres:password@postgres:5432/zauba_db
BASE_URL=https://comtradeapi.un.org/public/v1/preview/C/A/HS
API_HOST=0.0.0.0
API_PORT=8000
SCRAPER_SCHEDULE=0 2 * * *
```

| Variable         | Description                  |
| ---------------- | ---------------------------- |
| DATABASE_URL     | PostgreSQL connection string |
| BASE_URL         | UN Comtrade API endpoint     |
| API_HOST         | FastAPI host                 |
| API_PORT         | FastAPI port                 |
| SCRAPER_SCHEDULE | Automated ETL schedule       |

---

# ▶️ Steps to Run the Project Locally

## 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd zauba-trade-intelligence
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file using the environment variables above.

---

## 5. Start Docker Services

```bash
docker compose up --build
```

---

## 6. Load Data into PostgreSQL

Open a new terminal and run:

```bash
docker exec -it zauba_fastapi python -m pipeline.load_to_db
```

---

## 7. Access Applications

### FastAPI Swagger Docs

```text
http://localhost:8000/docs
```

### Streamlit Dashboard

```text
http://localhost:8501
```

---

# 🌐 Deployment Output

## FastAPI Interface

Provides business-consumable trade analytics APIs.

## Streamlit Dashboard

Provides visual business intelligence dashboards with live database integration.

Both interfaces are dynamic and reflect updated database records.

---

# 📈 Future Improvements

* ML-based anomaly detection
* Trade forecasting models
* Airflow orchestration
* Cloud deployment (AWS/GCP/Azure)
* Authentication & user roles
* Advanced BI dashboards
* Real-time streaming ingestion

---

# 👨‍💻 Author

I am moulicharan built this as a Data Engineering assignment project focused on designing a scalable and production-style B2B trade intelligence pipeline.
