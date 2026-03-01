import time
import psutil
import os
import csv
from sqterm.extras import loading
from sqterm.extras.autocomplete import CACHE

def info():
    return '"EXPORTCSV" - Exports a table to a CSV file'

def main(state , i):
    c = state["cursor"]

    c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    if sf4 == 0:
        print("No tables found!")
        return

    else:        
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        print("=== Tables: ===")
        print('')

        for item in tables:
            print("     ", item[0])
            CACHE.append(item[0])
        print('')

        table_name = input("Which table would you like to export as a CSV?: ")

    path = input("Full path to folder which you'd like the table exported: ")

    if path == "":
        os.makedirs("exports", exist_ok=True)
        path = os.path.abspath('exports/')

    try:
        loading.loading()
        start_mem = psutil.Process().memory_info().rss / 1024 / 1024
        start = time.perf_counter()

        formatted_headers = []
        headers = c.execute(f"SELECT name FROM pragma_table_info('{table_name}')").fetchall()
        for name in headers:
            formatted_headers.append(str(name)[:-2].strip("(").strip("'"))

        data = c.execute(f"SELECT * FROM {table_name}").fetchall()

        with open(f"{path}/exported{table_name}.csv", "w") as file:
            writer = csv.writer(file)

            writer.writerow(formatted_headers)

            for line in data:
                writer.writerow(line)

        end = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss / 1024 / 1024
        length = end - start
        mem_used = end_mem - start_mem
        loading.stop()
        CACHE.clear()
        print("Exported! Time to perform export:", f"{length:.2f}", 's', '|', "RAM Used:", f"{mem_used:.2f}", 'MB')

    except Exception as e:
        loading.stop()
        CACHE.clear()
        print("An error has occured! Problem:", e)

