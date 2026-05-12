import os

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create database connection
engine = create_engine(DATABASE_URL)

# Streamlit page config
st.set_page_config(
    page_title="B2B Trade Intelligence Dashboard",
    layout="wide"
)

st.title("🌍 B2B Trade Intelligence Dashboard")

# Load data from PostgreSQL
@st.cache_data
def load_data():

    query = "SELECT * FROM trade_records"

    df = pd.read_sql(query, engine)

    return df


df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

years = sorted(df["period"].unique())

selected_year = st.sidebar.selectbox(
    "Select Year",
    years
)

reporters = sorted(df["reporter_name"].unique())

selected_reporter = st.sidebar.selectbox(
    "Select Reporter Country",
    reporters
)

flows = sorted(df["flow_type"].unique())

selected_flow = st.sidebar.selectbox(
    "Select Flow Type",
    flows
)

# Apply filters
filtered_df = df[
    (df["period"] == selected_year) &
    (df["reporter_name"] == selected_reporter) &
    (df["flow_type"] == selected_flow)
]

# KPI metrics
total_trade_value = filtered_df["trade_value_usd"].sum()

total_quantity = filtered_df["quantity"].sum()

total_weight = filtered_df["net_weight_kg"].sum()

# KPI row
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Trade Value (USD)",
    f"${total_trade_value:,.0f}"
)

col2.metric(
    "Total Quantity",
    f"{total_quantity:,.0f}"
)

col3.metric(
    "Total Net Weight (KG)",
    f"{total_weight:,.0f}"
)

st.divider()

# Top products chart
top_products = (
    filtered_df.groupby("cmd_desc")["trade_value_usd"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="cmd_desc",
    y="trade_value_usd",
    title="Top Products by Trade Value"
)

st.plotly_chart(fig_products, use_container_width=True)

# Top partner countries chart
top_partners = (
    filtered_df.groupby("partner_name")["trade_value_usd"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_partners = px.pie(
    top_partners,
    names="partner_name",
    values="trade_value_usd",
    title="Top Trading Partners"
)

st.plotly_chart(fig_partners, use_container_width=True)

# Data table
st.subheader("Filtered Trade Records")

st.dataframe(filtered_df)