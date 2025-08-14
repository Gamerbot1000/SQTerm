import os

def clearscreen(db_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"========== Editing: {db_name}.db ==========")
    print("")