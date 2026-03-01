import psutil
import time
from sqterm.extras import loading

def info():
    return '"RUNSQL" - Run an external .sql file'

def main(state, i):
    c = state["cursor"]

    path = input("Path to .sql file: ")

    try:
        loading.loading()
        start_mem = psutil.Process().memory_info().rss / 1024 / 1024
        start = time.perf_counter()

        with open(path, "r") as f:
            sql = f.read()

        c.executescript(sql)
        print("Script Executed!")
        output = c.fetchall()
        print("Script Output:", output)

        end = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss / 1024 / 1024 / 1024
        length = end - start
        mem_used = end_mem - start_mem
        loading.stop()
        print("Time to execute:", f"{length:.2f}", "s", "|", "RAM used:", f"{mem_used:.2f}", "MB")

    except Exception as e:
        loading.stop()
        end = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss / 1024 / 1024
        print("An error has occured! Problem:", e)