import os

def info():
    return '"DIR" - Shows the directories of the databases and exports folders'

def main(state, i):

    print("Databases folder path:", os.path.abspath('databases/'))
    print("Exports folder path:", os.path.abspath('exports/'))
    print("Commands folder path:", os.path.abspath('commands/'))