import time
import psutil
import csv
from sqterm.extras import loading
from sqterm.extras.autocomplete import CACHE



def info():
    return '"IMPORTCSV" - Imports a CSV file as a new table'

def main(state , i):
    c = state["cursor"]

    path = input("Path to CSV file: ")
    choice = input("Import data to existing table or create new? (e/n): ")

    if choice.lower() == "e":

        sf1 = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
        sf2 = c.fetchall()
        sf3 = sf2[0]
        sf4 = sf3[0]

        if sf4 == 0:
            print("No data found!")

        else:
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = c.fetchall()
            print("=== Tables: ===")
            print('')
            for item in tables:
                print("     ", item[0])
                CACHE.append(item[0])
            print('')
            table_name = input("Name of the table you wish to import data to: ")
            CACHE.clear()

    elif choice.lower() == "n":
        table_name = input("Name of the new table to be created: ")
    
    else:
        print("Invalid choice!")
        return

    try:

        with open(path, "r") as file:
            content = csv.reader(file)
            
            headers = ""

            for num, line in enumerate(content):
                if num == 0 and choice.lower() == "n":
                    for item in line:
                        headers += f"'{item}' TEXT, "
                    headers_final = f"CREATE TABLE {table_name} ({headers[:-2]})"
                    c.execute(headers_final)

                if num > 0:
                    loading.loading()
                    start_mem = psutil.Process().memory_info().rss / 1024 / 1024
                    start = time.perf_counter()



                    insert = f"INSERT INTO {table_name} VALUES ({str(line).strip("[]")})"
                    c.execute(insert)

        end = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss / 1024 / 1024
        length = end - start
        mem_used = end_mem - start_mem
        loading.stop()
        print("Imported! Time to perform import:", f"{length:.2f}", 's', '|', "RAM Used:", f"{mem_used:.2f}", 'MB')

    except Exception as e:
        c.execute(f'DROP TABLE IF EXISTS "{table_name}";')
        loading.stop()
        print(f"An error has occured at row Problem:", e)