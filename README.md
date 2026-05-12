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

### 📈 Analyze Import/Export Trends

The system continuously collects structured international trade data and stores it in a centralized PostgreSQL database. Businesses can analyze historical trade patterns across years, countries, and product categories.

This helps organizations:

* Understand how trade volumes change over time
* Identify growing or declining markets
* Detect seasonal or long-term trade trends
* Support strategic sourcing and export planning

For example, a company exporting electronics can track how export value changes across different countries over multiple years and identify emerging high-demand regions.

---

### 🌍 Identify Major Trading Partners

The dashboard and APIs allow businesses to analyze which countries are the most significant importers or exporters for specific products.

This provides insights such as:

* Top partner countries by trade value
* Dependence on specific trade regions
* Market diversification opportunities
* Potential international expansion targets

Businesses can use these insights to strengthen supply chain decisions, optimize logistics planning, and identify new trade relationships.

---

### 📦 Monitor Product-Level Trade Flows

Trade records are categorized using HS (Harmonized System) product codes, enabling product-specific intelligence.

The platform helps businesses:

* Track trade flow for specific product categories
* Compare import vs export performance
* Measure product demand across countries
* Analyze product-wise trade value and quantity

This is especially useful for manufacturers, exporters, wholesalers, and supply chain teams who need product-level market visibility.

---

### 📊 Build Trade Intelligence Dashboards for Decision-Making

The Streamlit dashboard converts raw trade data into interactive business intelligence visualizations.

Using filters, KPI metrics, and charts, decision-makers can quickly explore:

* Total trade value
* Top products
* Major trading partners
* Country-specific trade insights
* Import/export comparisons

Instead of manually analyzing raw CSV files or API responses, businesses receive a centralized analytics platform that supports faster and more data-driven decisions.

---

### 🚀 Why This Project Is Useful

International trade datasets are often large, inconsistent, and difficult to process manually. This project solves that challenge by building a complete automated ETL pipeline.

The platform:

* Automates data ingestion from public trade APIs
* Cleans and standardizes raw records
* Stores data in a scalable relational database
* Provides APIs for analytics consumption
* Enables dashboard-based business intelligence
* Supports automated scheduling using APScheduler
* Uses Docker for reproducible deployment

This makes the system useful for:

* Trade intelligence platforms
* Supply chain analytics
* Import/export businesses
* Market research teams
* Economic and trade analysis
* Data-driven business strategy

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

# 📈 Future Improvements

* Machine learning anomaly detection
* Trade forecasting models
* Authentication and user roles
* Advanced BI dashboards
* Cloud deployment (AWS/GCP/Azure)
* Airflow orchestration

---

# 👨‍💻 Author

I am Moulicharan built this as a Data Engineering assignment project.
