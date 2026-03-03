import os
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.shortcuts import CompleteStyle
from sqterm.extras import art
from sqterm.extras.colors import *
from sqterm.extras.autocomplete import completer, history

def user_input(state):
    name = state["name"]

    text = ANSI(f"{GREEN}sqterm{RESET}{DIM}@{RESET}{CYAN}{os.path.basename(name)}:{RESET} ")
                
    i = prompt( 

        text,
        completer=completer, 
        history=history, 
        complete_style=CompleteStyle.READLINE_LIKE, 
        complete_while_typing=False
        
                )

    return i

def db_name():
    n = input("Enter .db file name or path to .db file: ")
    if os.path.isfile(n) == True:
        pass
    else:
        n = n.lower()
        if n.endswith(".db"):
            n = n[:-3]
    return n