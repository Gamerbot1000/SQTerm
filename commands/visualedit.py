import sqlite3
from tabulate import tabulate
import keyboard
import time
import os
from commands import clearscreen
from extras import loading

def visual_edit(conn, c, db_name):

    sf1 = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    if sf4 == 0:
        print("No data found! To enter 'VISUALEDIT' mode, you need to create a table first.")
        
    else:

        def highlight_green(text):
            return f"\033[92m{text}\033[0m"

        table1 = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table2 = c.fetchall()
        print('')
        print("=== Tables: ===")
        print('')
        for item in table2:
            print("     ", item[0])
        print("")

        try:
            table_name = input("Name of the table you wish to edit: ")
            command = f"SELECT COUNT(*) FROM {table_name};"
            commandex = c.execute(command)
            rowcount1 = c.fetchall()
            rowcount = rowcount1[0]
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\033[2J", end="")

            x = 0
            y = 0

            print('\033[?25l', end='')

            print(f"Rows available: {rowcount[0]}")
            q1 = input("Start editing from row: ")
            q1f = str(int(q1)-1)
            q2 = input("Row limit (15 max recommended): ")
            q2f = str(int(q2)+1)

            c.execute("BEGIN;")

            def print_table():
                command1 = f"SELECT * FROM {table_name} LIMIT {q2f} OFFSET {q1f}"
                row1 = c.execute(command1)
                row2 = c.fetchall()
                command2 = f"PRAGMA table_info({table_name})"
                column1 = c.execute(command2)
                columns = [col[1] for col in c.fetchall()]
                row2[x] = list(row2[x])
                row2[x][y] = highlight_green(text=row2[x][y])

                print('\033[H\033[J', end='')
                print("====== Table Edit Mode ======")
                print('')
                print("[F1] - Edit cell, [F2] - Add row, [F3] - Add column, [F4] - Save, [F5] - Delete row")
                print("Press UP/DOWN to move vertically, LEFT/RIGHT to move horizontally")
                print("Press ESC to exit")
                print('')
                print(tabulate(row2, headers=columns, tablefmt="grid"))
                print(f"\nRow: {x+1} | Column: {y+1} (<-- Real | Raw -->) Row: {x} | Column: {y}")

                return row2, columns                

            row2, columns = print_table()

            while True:

 

                

                if keyboard.is_pressed('down'):
                    x += 1
                    if x >= len(row2):
                        x = 0
                    print_table()
                    time.sleep(0.1)
                elif keyboard.is_pressed('up'):
                    x -= 1
                    if x < 0:
                        x = len(row2) - 1
                    print_table()
                    time.sleep(0.1)
                elif keyboard.is_pressed('right'):
                    y += 1
                    if y >= len(columns):
                        y = 0
                    print_table()
                    time.sleep(0.1)
                elif keyboard.is_pressed('left'):
                    y -= 1
                    if y < 0:
                        y = len(columns) - 1
                    print_table()
                    time.sleep(0.1)
                elif keyboard.is_pressed('f1'):
                    i = input('Update to: ')
                    if i == '':
                        pass
                    else:
                        command3 = f"UPDATE {table_name} SET {columns[y]} = '{i}' WHERE {columns[y+1]} = '{row2[x][y+1]}';"
                        ex = c.execute(command3)
                    print('\033[?25l', end='')
                    row2, columns = print_table()
                elif keyboard.is_pressed('f2'):
                    values = []
                    print("=== Create new row ===")
                    for i in range (0, len(columns)):
                        inp = input(f'Set {columns[i]} to: ')
                        values.append("'"+inp+"'")
                    values_str = ", ".join(values)
                    columns_str = ", ".join(columns)
                    command4 = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});"
                    ex2 = c.execute(command4)
                    print('\033[?25l', end='')
                    row2, columns = print_table()
                elif keyboard.is_pressed('f3'):
                    print("=== Create new column ===")
                    inp = input('Column name: ')
                    inp2 = input('Column type: ')
                    command5 = f"ALTER TABLE {table_name} ADD COLUMN {inp} {inp2};"
                    ex3 = c.execute(command5)
                    print('\033[?25l', end='')
                    row2, columns = print_table()
                elif keyboard.is_pressed('f4'):
                    conn.commit()
                elif keyboard.is_pressed('f5'):
                    inp = input("Delete row where: ")
                    inp2 = input("Equals: ")
                    command6 = f"DELETE FROM {table_name} WHERE {inp} = '{inp2}';"
                    ex4 = c.execute(command6)
                    print('\033[?25l', end='')
                    row2, columns = print_table()

                elif keyboard.is_pressed('esc'):
                    conn.rollback()
                    clearscreen.clearscreen(db_name)
                    print('\033[?25h', end='')
                    break

        except Exception as e:
            print("An error has occured! Problem:", e)
            print("Exiting VISUALEDIT mode...")
            loading.loading()
            time.sleep(2.5) # This time.sleep is to give the user time to read the error message
            loading.stop()
            clearscreen.clearscreen(db_name)
            print('\033[?25h', end='')

