import json
import os
import logging
import pandas as pd
from datetime import datetime, timezone

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Complete country code mapping
FULL_COUNTRY_CODES = {
    0: "World", 4: "Afghanistan", 8: "Albania", 12: "Algeria",
    24: "Angola", 28: "Antigua and Barbuda", 32: "Argentina",
    36: "Australia", 40: "Austria", 50: "Bangladesh", 56: "Belgium",
    64: "Bhutan", 68: "Bolivia", 76: "Brazil", 100: "Bulgaria",
    116: "Cambodia", 124: "Canada", 144: "Sri Lanka", 152: "Chile",
    156: "China", 170: "Colombia", 191: "Croatia", 196: "Cyprus",
    203: "Czech Republic", 208: "Denmark", 218: "Ecuador", 818: "Egypt",
    231: "Ethiopia", 246: "Finland", 250: "France", 276: "Germany",
    288: "Ghana", 300: "Greece", 356: "India", 360: "Indonesia",
    364: "Iran", 368: "Iraq", 372: "Ireland", 376: "Israel",
    380: "Italy", 388: "Jamaica", 392: "Japan", 400: "Jordan",
    398: "Kazakhstan", 404: "Kenya", 408: "North Korea", 410: "South Korea",
    414: "Kuwait", 422: "Lebanon", 458: "Malaysia", 484: "Mexico",
    504: "Morocco", 528: "Netherlands", 554: "New Zealand", 566: "Nigeria",
    578: "Norway", 586: "Pakistan", 604: "Peru", 608: "Philippines",
    616: "Poland", 620: "Portugal", 634: "Qatar", 642: "Romania",
    643: "Russia", 682: "Saudi Arabia", 710: "South Africa", 724: "Spain",
    144: "Sri Lanka", 752: "Sweden", 756: "Switzerland", 764: "Thailand",
    792: "Turkey", 784: "UAE", 800: "Uganda", 804: "Ukraine",
    826: "United Kingdom", 840: "United States", 704: "Vietnam",
    887: "Yemen", 894: "Zambia", 716: "Zimbabwe"
}

def load_latest_raw_file() -> list:
    data_dir = "data"
    files = [f for f in os.listdir(data_dir) if f.startswith("raw_trade_data")]
    if not files:
        logger.error("No raw data files found")
        return []
    latest = sorted(files)[-1]
    path = os.path.join(data_dir, latest)
    logger.info(f"Loading {path}")
    with open(path) as f:
        return json.load(f)

def clean_data(records: list) -> pd.DataFrame:
    df = pd.DataFrame(records)
    logger.info(f"Raw records: {len(df)}")

    # Decision 1: Drop rows where trade_value_usd is missing or zero
    before = len(df)
    df = df[df["trade_value_usd"].notna() & (df["trade_value_usd"] > 0)]
    logger.info(f"Dropped {before - len(df)} rows with missing/zero trade value")

    # Decision 2: Fill unknown partner names using full country map
    df["partner_name"] = df["partner_code"].apply(
        lambda x: FULL_COUNTRY_CODES.get(int(x), "Unknown") if pd.notna(x) else "Unknown"
    )

    # Decision 3: Fill unknown reporter names
    df["reporter_name"] = df["reporter_code"].apply(
        lambda x: FULL_COUNTRY_CODES.get(int(x), "Unknown") if pd.notna(x) else "Unknown"
    )

    # Decision 4: Fill missing weight and quantity with 0
    df["net_weight_kg"] = df["net_weight_kg"].fillna(0)
    df["quantity"] = df["quantity"].fillna(0)

    # Decision 5: Standardise period to integer year
    df["period"] = df["period"].astype(int)

    # Decision 6: Standardise trade value to float rounded to 2 decimals
    df["trade_value_usd"] = df["trade_value_usd"].astype(float).round(2)

    # Decision 7: Drop duplicates
    before = len(df)
    df = df.drop_duplicates(subset=["period", "reporter_code", "partner_code", "cmd_code", "flow_code"])
    logger.info(f"Dropped {before - len(df)} duplicate rows")

    # Decision 8: Add cleaned_at timestamp
    df["cleaned_at"] = datetime.now(timezone.utc).isoformat()

    logger.info(f"Clean records: {len(df)}")
    return df

def save_cleaned_data(df: pd.DataFrame) -> str:
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    path = f"data/cleaned_trade_data_{timestamp}.csv"
    df.to_csv(path, index=False)
    logger.info(f"Saved cleaned data to {path}")
    return path

def run_cleaner() -> pd.DataFrame:
    records = load_latest_raw_file()
    if not records:
        return pd.DataFrame()
    df = clean_data(records)
    save_cleaned_data(df)
    return df

if __name__ == "__main__":
    run_cleaner()