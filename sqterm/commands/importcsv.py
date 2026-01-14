import petl as etl
import time
import psutil
import sqlalchemy
from sqterm.extras import loading

def info():
    return '"IMPORTCSV" - Imports a CSV file as a new table'


def main(state, i):
    conn = state["conn"]
    c = state["cursor"]

    path = input("Path to CSV file: ")

    try:
        csv = etl.fromcsv(path)
        table_name = input("What would you like to name the new table?: ")
        start_mem = psutil.Process().memory_info().rss / 1024 / 1024
        start = time.perf_counter()
        loading.loading()
        etl.todb(csv, conn, table_name, create=True)
        end = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss / 1024 / 1024
        length = end - start
        mem_used = end_mem - start_mem
        loading.stop()
        print("Imported! Time to perform import:", length, 's', '|', "RAM Used:", mem_used, 'MB')
    except Exception as e:
        c.execute(f'DROP TABLE IF EXISTS "{table_name}";')
        loading.stop()
        print("An error has occured! Problem:", e)
