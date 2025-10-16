import psutil
import time
from extras import loading
from tabulate import tabulate

def executer(c, i):



            try:
                loading.loading()
                start_mem = psutil.Process().memory_info().rss / 1024 / 1024
                start = time.perf_counter()
                c.execute(i)

            except Exception as e:
                loading.stop()
                end = time.perf_counter()
                end_mem = psutil.Process().memory_info().rss / 1024 / 1024
                print("An error has occured! Problem:", e)

            else:        
                
                print("Command Executed!")
                output = c.fetchall()
                try:
                    c.execute(f"EXPLAIN QUERY PLAN {i}")
                    tble1 = c.fetchall()
                    for row in tble1:
                        last = (row[-1])
                    last_s = last.split()
                    tble2 = last_s[-1]
                    clmn1 = f"PRAGMA table_info({tble2})"
                    clmn2 = c.execute(clmn1)
                    clmn3 = c.fetchall()
                    columns = [col[1] for col in clmn3]
                    print('')
                    print(tabulate(output, headers=columns, tablefmt="grid"))
                    print('')
                    print(f"Raw output: {output}")
                    print("")

                except Exception:
                    pass
                    print("Command Output:", output)
                    
                end = time.perf_counter()
                end_mem = psutil.Process().memory_info().rss / 1024 / 1024
                length = end - start
                mem_used = end_mem - start_mem
                loading.stop()
                print("Time to execute:", length, "s", "|", "RAM used:", mem_used, "MB")