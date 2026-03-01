from tabulate import tabulate

def info():
    return '"DUMPDATA" - Dumps all the data in the database (Not reccomended for large databases)'

def main(state, i):
    c = state["cursor"]

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()

    if tables == []:
        print("No tables found!")
        return

    else:     

        for item in tables:
            print('')
            print(f'=== Table "{item[0]}" Data ===')

            command1 = f"SELECT * FROM {item[0]};"
            row1 = c.execute(command1)
            row2 = c.fetchall()
                    
            command2 = "PRAGMA table_info(" + item[0] + ")"
            column1 = c.execute(command2)
            columns = [col[1] for col in c.fetchall()]
                    
            print('')
            print(tabulate(row2, headers=columns, tablefmt="rounded_grid"))
            print('')