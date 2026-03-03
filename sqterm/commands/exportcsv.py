import time
import psutil
import os
import csv
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.completion import WordCompleter
from sqterm.extras import loading


def info():
    return '"EXPORTCSV" - Exports a table to a CSV file'

def main(state , i):
    c = state["cursor"]

    CACHE = []

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()

    if tables == []:
        print("No tables found!")
        return

    else:        
        print("=== Tables: ===")
        print('')

        for item in tables:
            print("     ", item[0])
            CACHE.append(item[0])
        print('')

        completer = WordCompleter(CACHE, ignore_case=True)

        table_name = prompt("Which table would you like to export as a CSV?: ", completer=completer, complete_style=CompleteStyle.READLINE_LIKE, complete_while_typing=False)

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

