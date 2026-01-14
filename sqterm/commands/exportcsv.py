import petl as etl
import time
import psutil
import os
from sqterm.extras import loading
from sqterm.extras.autocomplete import CACHE

def info():
    return '"EXPORTCSV" - Exports a table to a CSV file'

def main(state, i):
    conn = state["conn"]
    c = state["cursor"]

    os.makedirs("exports", exist_ok=True)

    c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    if sf4 == 0:
        print("No tables found!")

    else:        
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        print("=== Tables: ===")
        print('')

        for item in tables:
            print("     ", item[0])
            CACHE.append(item[0])
        print('')

        table_name = input("Which table would you like to export to CSV?: ")

        try:
            path = input("Path to folder where CSV file will be saved (if left blank will be saved in SQTerm exports folder): ")
            if path == '':
                path = 'exports/'
            start_mem = psutil.Process().memory_info().rss / 1024 / 1024
            start = time.perf_counter()
            loading.loading()
            table = etl.fromdb(conn, f'SELECT * FROM "{table_name}";')
            etl.tocsv(table, f'{path}/{table_name}.csv')
            end = time.perf_counter()
            end_mem = psutil.Process().memory_info().rss / 1024 / 1024
            length = end - start
            mem_used = end_mem - start_mem
            loading.stop()
            CACHE.clear()
            print("Exported! Time to perform export:", length, 's', '|', "RAM Used:", mem_used, 'MB')
        except Exception as e:
            loading.stop()
            CACHE.clear()
            print("An error has occured! Problem:", e)