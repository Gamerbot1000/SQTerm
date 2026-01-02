from sqterm.extras import loading

def info():
    return '"INTEGRITYCHECK" - Checks if any data in the database is corrupt'

def main(state, i):
    c = state["cursor"]

    try:
        loading.loading()
        ex = c.execute("PRAGMA integrity_check;")
        ex2 = c.fetchall()
        loading.stop()
        if str(ex2) == "[('ok',)]":
            print("Passed!")
        else:
            print("Failed!", ex2)
    except Exception as e:
        print("Failed!", e)