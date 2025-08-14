import os

def changedb(i):

    if len(i) > 9:
        n = i[9:]
    else:
        n = input("Enter new .db file name: ")
    name = n + '.db'
    cs = input("Execute 'CLEARSCREEN' after .db file change? (y/n): ")
    if cs == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cs == 'n':
        print("")       
    else:
        print("Invalid choice! Pick only y/n")
    return n, name