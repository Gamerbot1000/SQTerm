import pandas as pd
import time
import psutil
from extras import loading

def exportcsv(c, conn, i):
     
    sf1 = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    if sf4 == 0:
        print("No data found!")

    else:
        if len(i) > 10:
            q = i[10:]
        else:        
            table1 = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table2 = c.fetchall()
            print('')
            print("==== Tables: ====")
            print('')

            for item in table2:
                print("     ", item[0])
                print('')
            q = input("Name of the table you wish to export: ")
        try:
            loading.loading()
            start_mem = psutil.Process().memory_info().rss / 1024 / 1024
            start = time.perf_counter()
            command3 = "SELECT * FROM" + (" " + q + ";")
            readex = pd.read_sql_query(command3, conn)
            readex.to_csv((f"exports/exported_{q}_table.csv"), index=False, encoding="utf-8")
            end = time.perf_counter()
            end_mem = psutil.Process().memory_info().rss / 1024 / 1024
            length = end - start
            mem_used = end_mem - start_mem
            loading.stop()
            print("Exported! Time to perform export:", length, 's', '|', "RAM Used:", mem_used, 'MB')
        except Exception as e:
            loading.stop()
            print("An error has occured! Problem:", e)