import os
from core import connector

def info():
    return '"CHANGEDB" - Switch the .db file you are editing'

def main(state, i):
    conn = state["conn"]

    n = input("Enter new .db file name: ")
    svq = input("Do you want to save the changes made in this database before switching? (y/n): ")
    if svq == 'y' or svq == 'Y':
        conn.commit()
        conn.close()
    elif svq == 'n' or svq == 'N':
        conn.close()    
    else:
        print("Invalid choice! Pick only y/n")

    clsq = input("Execute 'CLEARSCREEN' after .db file change? (y/n): ")
    if clsq == 'y' or clsq == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif clsq == 'n' or clsq == 'N':
        print("")       
    else:
        print("Invalid choice! Pick only y/n")
    
    name, conn, c = connector.connect(n)
    state["db_name"] = n
    state["name"] = name
    state["conn"] = conn
    state["cursor"] = c