import os
import time
from sqterm.extras.colors import *

def info():
    return '"DBSTATS" - Shows various stats about the database'

def main(state, i):
    name = state["name"]
    c = state["cursor"]


    print(f"{BOLD}==== Database Stats ===={RESET}")
    print("")


    print(f"{BLUE}Path to database:{RESET}   {name}")

    size = os.path.getsize(name) / 1024 / 1024
    print(f'{BLUE}Estimated size:{RESET}   {size:.2f} MB{RESET}')

    t = os.path.getmtime(name)
    now = time.time()
    diff = (now - t) / 60
    t_name = "minutes"
    if diff > 60:
        diff = diff / 60
        t_name = "hours"
    print(f"{BLUE}Last modified:{RESET}   {diff:.2f} {t_name} ago{RESET}")

    sf1 = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
    sf2 = c.fetchall()
    sf3 = sf2[0]
    sf4 = sf3[0]

    print(f"{BLUE}Number of tables:{RESET}   {sf4}")

    if sf4 > 0:
        print("")
        print(f"{BLUE}Tables:{RESET}")
        print("")
        sf5 = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        sf6 = sf5.fetchall()
        for i in sf6:
            print(f"{DIM} - {RESET}{i[0]}  {DIM}|{RESET}  {GREEN}{c.execute(f'SELECT COUNT(*) FROM {i[0]};').fetchall()[0][0]} rows{RESET}")


    print("")
    print(f"{BOLD}========================{RESET}")