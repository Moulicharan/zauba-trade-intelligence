# 🌍 B2B Trade Intelligence Pipeline

## 📌 Problem Statement

Businesses involved in global import/export operations often struggle to access structured and actionable trade intelligence data. Raw international trade datasets are massive, inconsistent, and difficult to analyze directly.

This project solves that problem by building an end-to-end B2B Trade Intelligence Pipeline that:

* Fetches international trade data from the UN Comtrade public API
* Cleans and standardizes raw trade records
* Stores structured data in PostgreSQL
* Exposes analytics APIs using FastAPI
* Visualizes trade insights through Streamlit dashboards
* Automates the ETL workflow using APScheduler

The platform enables businesses to:

* Analyze import/export trends
* Identify major trading partners
* Monitor product-level trade flows
* Build trade intelligence dashboards for decision-making

---

An end-to-end Data Engineering project that fetches global trade data from the UN Comtrade API, cleans and processes it, stores it in PostgreSQL, exposes analytics APIs using FastAPI, visualizes insights through Streamlit dashboards, and automates the ETL workflow using APScheduler.

---

# 🚀 Features

* Automated trade data scraping
* Data cleaning and deduplication
* PostgreSQL data warehouse
* FastAPI analytics APIs
* Streamlit interactive dashboard
* APScheduler ETL automation
* Dockerized deployment
* Modular production-style architecture

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
| SCRAPER_SCHEDULE | Daily ETL schedule           |

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

# ⚙️ ETL Pipeline Architecture

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

# 📊 Dashboard Features

* Filter by:

  * Year
  * Reporter Country
  * Flow Type
* KPI metrics
* Top products visualization
* Top trading partners
* Interactive charts

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

### Query Parameters

| Parameter | Example   |
| --------- | --------- |
| year      | 2014      |
| reporter  | China     |
| partner   | India     |
| product   | Computers |
| flow      | Export    |

---

# ▶️ How to Run the Project Locally

## 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd zauba-trade-intelligence
```

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file using the variables listed above.

## 5. Start Docker Services

```bash
docker compose up --build
```

## 6. Load Data into PostgreSQL

Open a new terminal and run:

```bash
docker exec -it zauba_fastapi python -m pipeline.load_to_db
```

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

# 🐳 Docker Setup

## Build and Start Containers

```bash
docker compose up --build
```

## Services

| Service    | Port |
| ---------- | ---- |
| FastAPI    | 8000 |
| Streamlit  | 8501 |
| PostgreSQL | 5433 |

---

# 🌐 Access URLs

## FastAPI Swagger Docs

```text
http://localhost:8000/docs
```

## Streamlit Dashboard

```text
http://localhost:8501
```

---

# 🧪 Sample Workflow

## Run Scraper

```bash
python -m scraper.scraper
```

## Run Cleaner

```bash
python -m cleaning.cleaner
```

## Load Data into PostgreSQL

```bash
python -m pipeline.load_to_db
```

## Start Scheduler

```bash
python -m pipeline.scheduler
```

---


# 👨‍💻 Author

I am moulicharan built this as a Data Engineering assignment project.
