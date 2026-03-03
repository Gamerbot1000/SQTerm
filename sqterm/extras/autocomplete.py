from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
import os

CALLOUTS = []
CACHE = []



dirs = os.listdir('commands')
for file in dirs:
    if file.endswith('.py') and file != '__init__.py':
        command = file[:-3]
        CALLOUTS.append(command.upper())

keywords = CALLOUTS
cache = CACHE

if CACHE:
    completer = WordCompleter(cache, ignore_case=True)
else:
    completer = WordCompleter(keywords, ignore_case=True)


history = FileHistory(".sqterm_history")