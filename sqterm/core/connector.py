import os
import sqlite3
from sqterm.core import inputs

def connect(db_name):
    if os.path.isfile(db_name) == True:
        name = db_name
    else:
        name = "databases/" + db_name + ".db"
    conn = sqlite3.connect(name)
    c = conn.cursor()
    return name, conn, c