import os
import importlib

def info():
    return '"HELP" - Explains all app commands'

def main(state, i):
    print("Available commands:")
    command = os.listdir('commands')
    for file in command:
        if ".py" in file:
            try:
                module = importlib.import_module(f"sqterm.commands.{file[:-3]}")
                if hasattr(module, "info"):
                    print("     " + module.info())
            except Exception as e:
                print(e)