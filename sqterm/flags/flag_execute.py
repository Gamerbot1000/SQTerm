import os
import sys
from sqterm.core import connector
from sqterm.core import executer

def info():
    return '"--execute [path] "[query]" — Runs an SQL query on the database at the given path and prints the result. Add --raw before the query to output raw results instead of the built-in executor.'


def main():

    try:
        
        if os.path.isfile(sys.argv[2]) == True:
            db_name = sys.argv[2]
        else:
            print("The supplied path is not a valid file!")
            sys.exit()
    
        name, conn, c = connector.connect(db_name)

        if len(sys.argv) > 3 and sys.argv[3] == "--raw":
            c.execute(sys.argv[4])
            print(c.fetchall())
        else:
            executer.executer(c, i=sys.argv[3])
    
        conn.commit()
        conn.close()
        sys.exit()

    except Exception as e:
        print("An error has occured! Problem:", e)
        sys.exit()