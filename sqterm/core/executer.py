import psutil
import time
from sqterm.extras import loading

def executer(c, i):

            try:
                loading.loading()
                start_mem = psutil.Process().memory_info().rss / 1024 / 1024
                start = time.perf_counter()
                c.execute(i)
                print("Command Executed!")
                output = c.fetchall()

                print("Command Output:", output)
                    
                end = time.perf_counter()
                end_mem = psutil.Process().memory_info().rss / 1024 / 1024
                length = end - start
                mem_used = end_mem - start_mem
                loading.stop()
                print("Time to execute:", length, "s", "|", "RAM used:", mem_used, "MB")

            except Exception as e:
                loading.stop()
                end = time.perf_counter()
                end_mem = psutil.Process().memory_info().rss / 1024 / 1024
                print("An error has occured! Problem:", e)