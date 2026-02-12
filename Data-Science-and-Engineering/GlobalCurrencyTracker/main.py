from environment_setup import setup_project
from api_manager import get_live_rates
from data_handler import process_and_save
from data_analyzer import analyze_user_investment


def run_app():
    print("\n--- GlobalCurrencyTracker Starting ---")

    # Step 1: Folders
    setup_project()

    # Step 2: Fetch
    print("Connecting to live market...")
    data = get_live_rates()

    # Step 3: Save
    if data:
        process_and_save(data)
        print("[SUCCESS]: Live data recorded to CSV.")

        # Step 4 :Analyzer
        analyze_user_investment()
    else:
        print("[FAIL]: Connection blocked. Check logs/error.log")




if __name__ == "__main__":
    run_app()