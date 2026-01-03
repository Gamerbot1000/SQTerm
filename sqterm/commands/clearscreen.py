import os

def info():
    return '"CLEARSCREEN" - Clears the previous commands'

def main(state, i):
    os.system('cls' if os.name == 'nt' else 'clear')