import os
from sqterm.extras import art
from sqterm.extras.colors import *

def user_input(state):
    name = state["name"]

    i = input(f"{GREEN}sqterm{RESET}{DIM}@{RESET}{CYAN}{os.path.basename(name)}:{RESET} ")
    return i

def db_name():
    n = input("Enter .db file name or path to .db file: ")
    if os.path.isfile(n) == True:
        pass
    else:
        n = n.lower()
        if n.endswith(".db"):
            n = n[:-3]
    return n