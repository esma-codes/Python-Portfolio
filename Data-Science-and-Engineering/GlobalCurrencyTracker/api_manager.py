import requests
from datetime import datetime

def get_live_rates():
    """Fetches real-time USD rates from the API."""
    url = "https://open.er-api.com/v6/latest/USD"

    try:
        # verify=False helps bypass your local SSL issues
        response = requests.get(url, timeout=15, verify=False)
        return response.json()
    except Exception as e:
        # Logs the error to a file if something goes wrong
        with open("logs/error.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()}: {str(e)}\n")
        return None