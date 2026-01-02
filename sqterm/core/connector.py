import os
import sqlite3

def connect(db_name):
    if os.path.isfile(db_name) == True:
        name = db_name
    else:
        name = "databases/" + db_name + ".db"
    conn = sqlite3.connect(name)
    c = conn.cursor()
    print(f"========== Editing: {name} ==========")
    print("")
    return name, conn, c