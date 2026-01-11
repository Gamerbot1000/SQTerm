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

def db_name_legacy():
    os.system('cls' if os.name == 'nt' else 'clear')
    size = os.get_terminal_size()
    if size.columns >= 148 and size.lines >= 15:
        welcome = art.get_art()
        print(welcome)
    else:
        print("==== Welcome to SQTerm ====")
    print("")
    print("Please enter the name of the .db file you want to work with.")
    print("If the file does not exist, it will be created.")
    print("")
    databases = os.listdir("databases")
    l = len(databases)
    if l == 0:
        pass
    else:
        print("List of available databases in the databases folder:")
        print("")
        for file in databases:
            if file.endswith(".db"):
                print(" - ", file)
    print("")
    n = input("Enter .db file name or path to .db file: ")
    if os.path.isfile(n) == True:
        pass
    else:
        n = n.lower()
        if n.endswith(".db"):
            n = n[:-3]
    os.system('cls' if os.name == 'nt' else 'clear')
    return n