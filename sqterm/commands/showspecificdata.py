from tabulate import tabulate

def info():
    return '"SHOWSPECIFICDATA" - Prints specific data from a chosen table'

def main(state, i):
    c = state["cursor"]

    sf1 = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    if sf4 == 0:
        print("No data found!")

    else:
        if len(i) > 17:
            q = i[17:]
        else:
            table1 = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table2 = c.fetchall()
            print('')
            print("=== Tables: ===")
            print('')
            for item in table2:
                print("     ", item[0])
            print("")
            q = input("Name of the table you wish to fetch data from: ")

        try:
            columnnames = c.execute(f"SELECT name FROM pragma_table_info('{q}');")
            columnnames1 = c.fetchall()
            print('')
            print("=== Columns in table", q + ": ===")
            print('')
            for col in columnnames1:
                print("     ", col[0])
            print("")
            q_col = input("Names of columns you wish to fetch data from (or press ENTER to select all): ")
            if q_col == "":
                q_col = "*"

            rowcount_ex = c.execute(f"SELECT COUNT(*) FROM {q};")
            rowcount1 = c.fetchall()
            rowcount = rowcount1[0]
            print(f"Rows available: {rowcount[0]}")
            q1 = input("Start from row: ")
            q1f = str(int(q1)-1)
            q2 = input("Row limit: ")
            q2f = str(int(q2)+1)
            command1 = f"SELECT {q_col} FROM {q} LIMIT {q2f} OFFSET {q1f}"
            row1 = c.execute(command1)
            row2 = c.fetchall()

            if q_col == "*":                
                command2 = "PRAGMA table_info(" + q + ")"
                column1 = c.execute(command2)
                columns = [col[1] for col in c.fetchall()]
            else:
                columns = [col.strip() for col in q_col.split(",")]
                            
            print('')
            print(tabulate(row2, headers=columns, tablefmt="grid"))
            print('')
        except Exception as e:
            print("An error has occured! Problem:", e)