# import pathlib
import sys
import os
from sqterm.__main__ import run_path

def info():
    return '"--open [path]" - Connects to the database at the specified path overriding the default prompt for a database path'


def main():
    path = sys.argv[2]
    db_path = os.path.join(run_path, path)

    if os.path.isfile(db_path) == True:
        db_name = db_path
    else:
        print("The supplied path is not a valid file!")
        sys.exit()
    return db_name