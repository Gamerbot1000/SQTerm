import sqlite3

def connect(db_name):
    name = "databases/" + db_name + ".db"
    conn = sqlite3.connect(name)
    c = conn.cursor()
    print(f"========== Editing: {db_name}.db ==========")
    print("")
    return name, conn, c