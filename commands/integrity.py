from extras import loading

def check(c):
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