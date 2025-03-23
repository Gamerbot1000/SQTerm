import pandas as pd
import time
import psutil
import os
from tabulate import tabulate
from extras import loading

def importcsv(conn):

    path = input("Path to CSV folder: ")

    try:

        loading.loading()
        read = pd.read_csv(path)
        csvname = os.path.splitext(os.path.basename(path))[0]
        row_count = len(read)
        loading.stop()
        if row_count < 1000:

            print("")
            print("=== CSV Table:", csvname, "===")
            print("")
            print(tabulate(read, headers='keys', tablefmt='grid'))
            print("")
        else:
            warning = input("This CSV file has 1000+ rows are you sure you want to print it? (y/n): ")
            if warning == 'y':

                print("")
                print("=== CSV Table:", csvname, "===")
                print("")
                print(tabulate(read, headers='keys', tablefmt='grid'))
                print("")

        q = input("Would you like to import this table to this .db file? (y/n): ")
        if q == 'y':

            table_name = input("Input new table name: ")
            loading.loading()
            start_mem = psutil.Process().memory_info().rss / 1024 / 1024
            start = time.perf_counter()
            read.to_sql(table_name, conn, if_exists="replace", index=False)
            end = time.perf_counter()
            end_mem = psutil.Process().memory_info().rss / 1024 / 1024
            length = end - start
            mem_used = end_mem - start_mem
            loading.stop()
            print("Imported! Time to perform import:", length, 's', '|', "RAM Used:", mem_used, 'MB')
    except Exception as e:
            print("An error has occured! Problem:", e)