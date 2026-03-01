import sys
import os
import importlib

def info():
    return '"--help" - Explains how to start the app and explains all available app flags'

def main():
    print("Type `sqterm` to run the program and be prompted for a path to a database.")
    print("Optionally, you can add flags to the command to run specific functions.")
    print("Available flags:")

    flags = os.listdir('flags')
    for file in flags:
        if ".py" in file:
            try:
                module = importlib.import_module(f"sqterm.flags.{file[:-3]}")
                if hasattr(module, "info"):
                    print("     " + module.info())
            except Exception as e:
                print(e)

    sys.exit()