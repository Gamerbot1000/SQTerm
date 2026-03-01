import psutil
import time
from sqterm.extras import loading
from sqterm.extras.colors import *
from tabulate import tabulate

def executer(c, i):

    try:
        if i == "":
            return

        loading.loading()
        start_mem = psutil.Process().memory_info().rss / 1024 / 1024
        start = time.perf_counter()
        c.execute(i)
        print("Command Executed!")
        output = c.fetchall()

        if i.upper().startswith("SELECT"):

            table_name = ""
            tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            for table in tables:
                if str(table[0]).upper() in i.upper():
                    table_name = table[0]
                    break
            if table_name == "":
                print("Command Output:", output)
                
                    
            if "*" not in i:
                included_headers = []
                headers = c.execute(f"SELECT name FROM pragma_table_info('{table_name}')").fetchall()
                for word in i.upper().split():
                    if str(word).endswith(","):
                        word = word[:-1]
                    for header in headers:
                        header = str(header[0])
                        if header.upper() == word:
                            included_headers.append(BOLD+header+RESET)
                    
                headers = included_headers
            else:
                headers = c.execute(f"SELECT name FROM pragma_table_info('{table_name}')").fetchall()
                formated_headers = []
                for header in headers:
                    formated_headers.append(BOLD+str(header[0])+RESET)
                headers = formated_headers

            print()
            print(tabulate(output, headers=headers, tablefmt="rounded_grid"))
            print()

            

        else:
            print("Command Output:", output)
            
        end = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss / 1024 / 1024
        length = end - start
        mem_used = end_mem - start_mem
        loading.stop()
        print("Time to execute:", f"{length:.2f}", "s", "|", "RAM used:", f"{mem_used:.2f}", "MB")

    except Exception as e:
        loading.stop()
        end = time.perf_counter()
        end_mem = psutil.Process().memory_info().rss / 1024 / 1024
        print("An error has occured! Problem:", e)