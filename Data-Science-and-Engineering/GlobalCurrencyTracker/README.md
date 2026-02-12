# GlobalCurrencyTracker 🌍💸

A professional Python-based Data Engineering pipeline that automates real-time exchange rate collection and provides interactive investment analysis.

## 🚀 Purpose
This project demonstrates an end-to-end **Data Pipeline** designed for financial tracking:
1.  **Data Acquisition**: Automatically fetching live USD exchange rates from a public API.
2.  **Data Persistence**: Transforming raw JSON responses into a structured, historical CSV database.
3.  **Modular Architecture**: Utilizing a decoupled system design for scalability and maintenance.
4.  **Financial Analysis**: An interactive module that calculates investment ROI (Return on Investment) based on real-time market data.

## 🛠️ Tech Stack & Skills
* **Python 3.x**: Core logic and object-oriented principles.
* **Requests Module**: Handling HTTP communication and bypassing SSL restrictions in restricted environments.
* **CSV & JSON**: Management of data storage and parsing.
* **Modular Programming**: Separation of concerns into distinct scripts (Setup, Fetch, Process, Analyze).

## 📂 Project Structure
```text
GlobalCurrencyTracker/
├── exchange_data/           # Local CSV database for exchange rates
├── logs/                    # System logs for error tracking
├── main.py                  # The central orchestrator (Entry point)
├── api_manager.py           # API connection and data retrieval
├── data_handler.py          # Data transformation and CSV storage
├── data_analyzer.py         # Interactive ROI analysis tool
├── environment_setup.py     # Initial folder and system initialization
└── requirements.txt         # Project dependencies


--- 🏦 Personal Investment Analyzer ---
Total TL invested: 200
USD rate at the time of purchase: 40

========================================
Purchased Amount : 5.00 USD
Current Market   : 43.67 TL
Initial Cost     : 200.00 TL
Current Value    : 218.33 TL
STATUS: PROFIT (+18.33 TL / %9.17) 🚀
========================================
