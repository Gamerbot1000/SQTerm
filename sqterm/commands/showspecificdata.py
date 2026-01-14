from tabulate import tabulate
from sqterm.extras.autocomplete import CACHE

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
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = c.fetchall()
            print("=== Tables: ===")
            print('')
            for item in tables:
                print("     ", item[0])
                CACHE.append(item[0])
            print('')
            q = input("Name of the table you wish to fetch data from: ")

        try:
            c.execute(f"SELECT name FROM pragma_table_info('{q}');")
            column_names = c.fetchall()
            print('')
            print("=== Columns in table", q + ": ===")
            print('')
            for col in column_names:
                print("     ", col[0])
                CACHE.append(col[0])
            print('')
            q_col = input("Names of columns you wish to fetch data from (or press ENTER to select all): ")
            if q_col == "":
                q_col = "*"

            c.execute(f"SELECT COUNT(*) FROM {q};")
            row_count = c.fetchall()
            row_count_fetch = row_count[0]
            print('')
            print(f"Rows available: {row_count_fetch[0]}")
            q1 = input("Start from row: ")
            q1f = str(int(q1)-1)
            q2 = input("Row limit: ")
            q2f = str(int(q2)+1)
            fetched_data = f"SELECT {q_col} FROM {q} LIMIT {q2f} OFFSET {q1f}"
            c.execute(fetched_data)
            rows = c.fetchall()

            if q_col == "*":                
                command2 = "PRAGMA table_info(" + q + ")"
                column1 = c.execute(command2)
                columns = [col[1] for col in c.fetchall()]
            else:
                columns = [col.strip() for col in q_col.split(",")]

            CACHE.clear()
                            
            print('')
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            print('')
        except Exception as e:
            CACHE.clear()
            print("An error has occured! Problem:", e)