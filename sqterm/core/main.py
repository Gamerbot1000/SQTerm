import os
import importlib
import sys
from sqterm.core import inputs
from sqterm.core import connector
from sqterm.core import executer
from sqterm.extras import autocomplete

def main_app():
    os.makedirs("databases", exist_ok=True)


    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]) == True:
        db_name = sys.argv[1]
    elif len(sys.argv) > 1 and sys.argv[1] == "--legacy":
        db_name = inputs.db_name_legacy()
    elif len(sys.argv) > 1 and os.path.isfile(sys.argv[1]) == False:
        print("Invalid argument, type 'sqterm [PATH_TO_DB]' or 'sqterm --legacy' for old database selection.")
        sys.exit()
    else:
        db_name = inputs.db_name()

    name, conn, c = connector.connect(db_name)

    autocomplete.completer()

    state = {
        "db_name": db_name,
        "name": name,
        "conn": conn,
        "cursor": c,
        "running": True,
    }

    while state["running"]:
        
        i = inputs.user_input(state)

        try:
            cmd = importlib.import_module(f"sqterm.commands.{i.split()[0].lower()}")
            cmd.main(state, i)

        except Exception as e:
            executer.executer(c, i)

if __name__ == "__main__":
    main_app()