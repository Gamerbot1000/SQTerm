import os
from sqterm.core import connector

def info():
    return '"CHANGEDB" - Switch the .db file you are editing'

def main(state, i):
    conn = state["conn"]

    if len(i) > 9:
        n = i[9:]
    else:
        n = input("Enter new .db file name: ")

    clsq = input("Execute 'CLEARSCREEN' after .db file change? (y/n): ")
    if clsq == 'y' or clsq == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif clsq == 'n' or clsq == 'N':
        pass       
    else:
        print("Invalid choice! Pick only y/n")
    
    name, conn, c = connector.connect(n)
    state["db_name"] = n
    state["name"] = name
    state["conn"] = conn
    state["cursor"] = c