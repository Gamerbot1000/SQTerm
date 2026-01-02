import time
import threading
import sys

done = False
t = None

def loading():
    global t, done
    done = False
    def loading2():
        while done == False:
            for i in ['.', '..', '...', '....']:
                if done:
                    break
                print(f"Loading{i:<4}", end='\r')
                time.sleep(0.5)
    t = threading.Thread(target=loading2)
    t.start()

def stop():
    global done, t
    done = True
    if t:
        t.join()
    print(' ' * 50, end='\r')