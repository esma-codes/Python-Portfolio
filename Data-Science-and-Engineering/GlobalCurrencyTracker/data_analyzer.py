import csv
import os


def analyze_user_investment():
    """Calculates profit/loss based on user investment and live market data."""
    print("\n--- 🏦 Personal Investment Analyzer ---")

    try:
        # User input for investment details
        total_investment_tl = float(input("Total TL invested: "))
        buying_rate = float(input("USD rate at the time of purchase: "))

        # Calculate the actual USD amount owned
        owned_usd = total_investment_tl / buying_rate
    except ValueError:
        print("[ERROR]: Please enter valid numeric values.")
        return

    file_path = "exchange_data/currency_history.csv"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = list(csv.DictReader(file))

            # Retrieve the most recent TRY rate from the dataset
            current_rate = 0
            for row in reversed(reader):
                if row["Target"] == "TRY":
                    current_rate = float(row["Value"])
                    break

            # Financial analysis logic
            current_portfolio_value = owned_usd * current_rate
            net_profit_loss = current_portfolio_value - total_investment_tl
            profit_percentage = (net_profit_loss / total_investment_tl) * 100

            print("\n" + "=" * 40)
            print(f"Purchased Amount : {owned_usd:.2f} USD")
            print(f"Current Market   : {current_rate:.2f} TL")
            print(f"Initial Cost     : {total_investment_tl:.2f} TL")
            print(f"Current Value    : {current_portfolio_value:.2f} TL")

            if net_profit_loss > 0:
                print(f"STATUS: PROFIT (+{net_profit_loss:.2f} TL / %{profit_percentage:.2f}) 🚀")
            else:
                print(f"STATUS: LOSS ({net_profit_loss:.2f} TL / %{profit_percentage:.2f}) 📉")
            print("=" * 40)

    except Exception as e:
        print(f"[ANALYSIS ERROR]: {e}")