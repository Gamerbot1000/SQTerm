import os
import importlib
from core import inputs
from core import connector
from core import executer

def main_app():

    os.system('cls' if os.name == 'nt' else 'clear')
    db_name = inputs.db_name()
    os.system('cls' if os.name == 'nt' else 'clear')
    name, conn, c = connector.connect(db_name)


    state = {
        "db_name": db_name,
        "name": name,
        "conn": conn,
        "cursor": c,
        "running": True,
    }

    while state["running"]:
        
        i = inputs.user_input()

        try:
            cmd = importlib.import_module(f"commands.{i.lower()}")
            cmd.main(state, i)

        except Exception as e:
            executer.executer(c, i)

if __name__ == "__main__":
    main_app()