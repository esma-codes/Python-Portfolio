import csv
import os
from datetime import datetime


def process_and_save(json_data):
    """Parses JSON and appends specific currency rates to a CSV."""
    path = "exchange_data/currency_history.csv"
    exists = os.path.exists(path)

    rates = json_data.get("rates", {})
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not exists:
            writer.writerow(["Timestamp", "Base", "Target", "Value"])

        # We focus on TRY and EUR for our first data set
        for target in ["TRY", "EUR"]:
            if target in rates:
                writer.writerow([timestamp, "USD", target, rates[target]])