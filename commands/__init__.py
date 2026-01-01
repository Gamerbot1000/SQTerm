import os
import importlib

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith('.py') and file not in ('__init__.py',):
        importlib.import_module(f'commands.{file[:-3]}')
