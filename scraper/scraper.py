import json
import os
import logging
from datetime import datetime
from scraper.utils import make_request, COUNTRY_CODES, HS_CODES, logger

BASE_URL = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

def build_url(reporter_code: int, cmd_code: str) -> str:
    return f"{BASE_URL}?reporterCode={reporter_code}&cmdCode={cmd_code}"

def fetch_trade_data(reporter_code: int, cmd_code: str) -> list:
    url = build_url(reporter_code, cmd_code)
    logger.info(f"Fetching: {url}")
    response = make_request(url)

    if not response or "data" not in response:
        logger.warning(f"No data for reporter={reporter_code}, cmd={cmd_code}")
        return []

    records = []
    for item in response.get("data", []):
        records.append({
            "period": item.get("period", None),
            "reporter_code": item.get("reporterCode", None),
            "reporter_name": COUNTRY_CODES.get(item.get("reporterCode"), "Unknown"),
            "flow_code": item.get("flowCode", None),
            "flow_type": "Import" if item.get("flowCode") == "M" else "Export",
            "partner_code": item.get("partnerCode", None),
            "partner_name": COUNTRY_CODES.get(item.get("partnerCode"), "Unknown"),
            "cmd_code": item.get("cmdCode", None),
            "cmd_desc": HS_CODES.get(cmd_code, "Unknown Product"),
            "trade_value_usd": item.get("primaryValue", None),
            "net_weight_kg": item.get("netWgt", None),
            "quantity": item.get("qty", None),
            "scraped_at": datetime.utcnow().isoformat()
        })

    logger.info(f"Fetched {len(records)} records")
    return records

def run_scraper() -> str:
    all_records = []

    for reporter_code in list(COUNTRY_CODES.keys())[:5]:
        for cmd_code in list(HS_CODES.keys())[:5]:
            records = fetch_trade_data(reporter_code, cmd_code)
            all_records.extend(records)

    os.makedirs("data", exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_path = f"data/raw_trade_data_{timestamp}.json"

    with open(output_path, "w") as f:
        json.dump(all_records, f, indent=2)

    logger.info(f"Saved {len(all_records)} records to {output_path}")
    return output_path

if __name__ == "__main__":
    run_scraper()