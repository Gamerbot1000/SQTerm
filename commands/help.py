import os
import commands

def info():
    return '"HELP" - Explains all app commands'

def main(state, i):
    print("Available commands:")
    command = os.listdir('commands')
    for file in command:
        if ".py" in file:
            try:
                print('     '+getattr(commands, file[:-3]).info())
            except:
                pass