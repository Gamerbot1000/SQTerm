import os
import time

def stats(c, db_name):
    print("")
    print("==== Database Stats ====")
    print("")
    sf1 = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    print(f"Tables ({sf4})")
    if sf4 > 0:
        print("")
        sf5 = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        sf6 = sf5.fetchall()
        for i in sf6:
            print(" - ",i[0])
        print("")

    size = os.path.getsize("databases/" + db_name + ".db") / 1024 / 1024
    print(f'Estimated size:     {size:.2f} MB')
    t = os.path.getmtime("databases/" + db_name + ".db")
    now = time.time()
    diff = (now - t) / 60
    t_name = "minutes"
    #if diff > 60:
        #diff = diff / 60
        #t_name = "hours"
    print(f"Last modified:      {diff:.2f} {t_name} ago")
    print("")
    print("========================")
    print("")