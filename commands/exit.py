import sys

def exit(conn):
    conn.commit()
    conn.close()
    sys.exit()