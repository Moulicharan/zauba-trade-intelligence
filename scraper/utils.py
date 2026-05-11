import time
import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

COUNTRY_CODES = {
    356: "India",
    156: "China",
    840: "United States",
    276: "Germany",
    392: "Japan",
    410: "South Korea",
    826: "United Kingdom",
    682: "Saudi Arabia",
    784: "UAE",
    764: "Thailand",
    458: "Malaysia",
    360: "Indonesia",
    704: "Vietnam",
    56: "Belgium",
    528: "Netherlands",
}

HS_CODES = {
    "8471": "Computers & Laptops",
    "8517": "Phones & Communication Devices",
    "2709": "Crude Oil",
    "3004": "Medicines & Pharmaceuticals",
    "7108": "Gold",
    "8703": "Motor Cars",
    "8542": "Electronic Integrated Circuits",
    "6110": "Textile & Apparel",
    "1001": "Wheat",
    "1511": "Palm Oil",
}

def make_request(url: str, retries: int = 3, delay: int = 2) -> dict:
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
    logger.error(f"All {retries} attempts failed for {url}")
    return {}