import os
import importlib
from sqterm.core import inputs
from sqterm.core import connector
from sqterm.core import executer

def main_app():
    os.makedirs("databases", exist_ok=True)
    os.makedirs("exports", exist_ok=True)


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
            cmd = importlib.import_module(f"sqterm.commands.{i.lower()}")
            cmd.main(state, i)

        except Exception as e:
            executer.executer(c, i)

if __name__ == "__main__":
    main_app()