import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

URL = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
EXCHANGE_RATE_CSV = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
TABLE_ATTRIBUTES = ["Name", "MC_USD_Billion"]
OUTPUT_CSV_PATH = './Largest_banks_data.csv'
DATABASE_NAME = 'Banks.db'
TABLE_NAME = 'Largest_banks'
LOG_FILE = 'code_log.txt'


def log_progress(message):
    timestamp_format = '%Y-%b-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} : {message}\n")
    print(f"{timestamp} : {message}")


def extract(url, table_attribs):
    try:
        log_progress("Extraction process started.")
        html_page = requests.get(url).text
        data = BeautifulSoup(html_page, 'html.parser')
        df = pd.DataFrame(columns=table_attribs)

        tables = data.find_all('tbody')
        rows = tables[0].find_all('tr')

        for row in rows:
            col = row.find_all('td')
            if len(col) != 0:
                # Banka adı ve Piyasa değeri (USD) temizlenerek alınıyor
                bank_name = col[1].find_all('a')[1].contents[0]
                market_cap = float(col[2].contents[0].strip())  # n karakterini strip ile siliyoruz
                new_row = {"Name": bank_name, "MC_USD_Billion": market_cap}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        log_progress("Extraction process completed.")
        return df
    except Exception as e:
        log_progress(f"Error during extraction: {e}")
        return pd.DataFrame(columns=table_attribs)


def transform(df, csv_path):
    log_progress("Transformation process started.")
    exchange_rate = pd.read_csv(csv_path)
    rates = exchange_rate.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * rates['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * rates['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * rates['INR'], 2) for x in df['MC_USD_Billion']]

    log_progress("Transformation process completed.")
    return df


def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)
    log_progress("Data saved to CSV file.")


def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    log_progress("Data loaded to Database as a table.")


def run_queries(query_statements, sql_connection):
    for query in query_statements:
        log_progress(f"Executing query: {query}")
        query_output = pd.read_sql(query, sql_connection)
        print(query_output)


log_progress("Preliminaries complete. Initiating ETL process.")

df = extract(URL, TABLE_ATTRIBUTES)
df = transform(df, EXCHANGE_RATE_CSV)

load_to_csv(df, OUTPUT_CSV_PATH)

conn = sqlite3.connect(DATABASE_NAME)
load_to_db(df, conn, TABLE_NAME)

queries = [
    "SELECT * FROM Largest_banks",
    "SELECT AVG(MC_GBP_Billion) FROM Largest_banks",
    "SELECT Name from Largest_banks LIMIT 5"
]
run_queries(queries, conn)

conn.close()
log_progress("ETL Process Complete.")