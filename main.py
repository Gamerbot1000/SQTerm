import os
from core import inputs
from core import connector
from commands import exit
from commands import clearscreen
from commands import executer
from commands import showdata
from commands import showspecificdata
from commands import changedb
from commands import importcsv
from commands import exportcsv
from commands import help
from commands import integrity
from commands import dbstats

os.system('cls' if os.name == 'nt' else 'clear')
db_name = inputs.db_name()
os.system('cls' if os.name == 'nt' else 'clear')
name, conn, c = connector.connect(db_name)


while True:
    
    i = inputs.user_input()

    if i == "EXIT":
        exit.exit(conn)

    elif i == "CLEARSCREEN":
        clearscreen.clearscreen(db_name)

    elif i == "SHOWDATA":
        showdata.showdata(c)
    
    elif i == "SHOWSPECIFICDATA":
        showspecificdata.showspecificdata(c)

    elif i == "CHANGEDB":
        n, name = changedb.changedb()
        db_name = n
        name, conn, c = connector.connect(db_name)

    elif i == "IMPORTCSV":
        importcsv.importcsv(conn)

    elif i == "EXPORTCSV":
        exportcsv.exportcsv(c, conn)

    elif i == "INTEGRITYCHECK":
        integrity.check(c)

    elif i == "DBSTATS":
        dbstats.stats(c, db_name)

    elif i == "HELP":
        help.help()

    else:
        executer.executer(c, i)