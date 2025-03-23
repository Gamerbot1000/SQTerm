def exit(conn):
    conn.commit()
    conn.close()
    quit()