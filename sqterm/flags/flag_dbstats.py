import os
import sys
from commands import dbstats
from core import connector
from sqterm.__main__ import run_path

def info():
    return '"--dbstats [path]" - Shows various stats about the database at the given path"'


def main():
    path = os.path.join(run_path, sys.argv[2])

    if os.path.isfile(path) == True:
            db_name = path
    else:
        print("The supplied path is not a valid file!")
        sys.exit()

    name, conn, c = connector.connect(db_name)

    state = {
        "name": name,
        "cursor": c
    }

    dbstats.main(state, i="")

    conn.close()
    sys.exit()

    