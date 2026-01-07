from tabulate import tabulate

def info():
    return '"SHOWDATA" - Prints all the data (Not reccomended for large databases)'

def main(state, i):
    c = state["cursor"]

    sf1 = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    if sf4 == 0:
        print("No data found!")
    else:
                
                
        table1 = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table2 = c.fetchall()
                

        for item in table2:
            print('')
            print(f'=== Table {item[0]} Data ===')

            command1 = f"SELECT * FROM {item[0]};"
            row1 = c.execute(command1)
            row2 = c.fetchall()
                    
            command2 = "PRAGMA table_info(" + item[0] + ")"
            column1 = c.execute(command2)
            columns = [col[1] for col in c.fetchall()]
                    
            print('')
            print(tabulate(row2, headers=columns, tablefmt="grid"))
            print('')