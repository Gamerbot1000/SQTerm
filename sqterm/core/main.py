import os
import importlib
import sys
from sqterm.core import inputs
from sqterm.core import connector
from sqterm.core import executer
from sqterm.extras import autocomplete

def main_app():
    os.makedirs("databases", exist_ok=True)

    db_name = None

    if len(sys.argv) > 1:
        try:
            flag = importlib.import_module(f"sqterm.flags.{sys.argv[1].replace('--', 'flag_').lower()}")
            function_flag = flag.main()

            if function_flag != None and os.path.isfile(function_flag) == True:
                db_name = function_flag
                

        except Exception:
            print("Invalid or broken flag provided!")
            sys.exit()

    if db_name == None:
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