import os
from extras import art
from commands import directories

def user_input():
    i = input("Your Command: ")
    return i

def db_name():
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
    folder_path = "databases"
    file_names = os.listdir(folder_path)
    l = len(file_names)
    if l == 0:
        pass
    else:
        print("List of available databases:")
        print("")
        for x in range(1, l):
            print(" - ", file_names[x])
    print("")
    print("Make sure not to include the .db extension in the name.")
    print("")
    n = input("Enter .db file name: ")
    return n