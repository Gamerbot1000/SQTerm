import os

def info():
    return '"CLEARSCREEN" - Clears the previous commands'

def main(state, i):
    name = state["name"]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"========== Editing: {name} ==========")
    print("")