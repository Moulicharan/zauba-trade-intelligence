from pathlib import Path

import pandas as pd

from api.database import SessionLocal
from api.models import TradeRecord


DATA_DIR = Path("data")


def get_latest_cleaned_file():

    cleaned_files = sorted(
        DATA_DIR.glob("cleaned_trade_data_*.csv"),
        reverse=True
    )

    if not cleaned_files:
        raise FileNotFoundError(
            "No cleaned CSV files found in data/"
        )

    return cleaned_files[0]


def load_csv_to_postgres():

    latest_file = get_latest_cleaned_file()

    print(f"Loading file: {latest_file}")

    df = pd.read_csv(latest_file)

    db = SessionLocal()

    try:

        inserted_count = 0

        for _, row in df.iterrows():

            # Prevent duplicate inserts
            existing_record = db.query(TradeRecord).filter(
                TradeRecord.period == row["period"],
                TradeRecord.reporter_code == row["reporter_code"],
                TradeRecord.partner_code == row["partner_code"],
                TradeRecord.cmd_code == row["cmd_code"],
                TradeRecord.flow_code == row["flow_code"]
            ).first()

            if existing_record:
                continue

            trade = TradeRecord(
                period=row["period"],
                reporter_code=row["reporter_code"],
                reporter_name=row["reporter_name"],
                flow_code=row["flow_code"],
                flow_type=row["flow_type"],
                partner_code=row["partner_code"],
                partner_name=row["partner_name"],
                cmd_code=row["cmd_code"],
                cmd_desc=row["cmd_desc"],
                trade_value_usd=row["trade_value_usd"],
                net_weight_kg=row["net_weight_kg"],
                quantity=row["quantity"],
                scraped_at=pd.to_datetime(row["scraped_at"]),
                cleaned_at=pd.to_datetime(row["cleaned_at"])
            )

            db.add(trade)

            inserted_count += 1

        db.commit()

        print(f"Inserted {inserted_count} records into PostgreSQL")

    except Exception as e:

        db.rollback()

        print(f"Error: {e}")

    finally:

        db.close()


if __name__ == "__main__":

    load_csv_to_postgres()