import readline
import os

CALLOUTS = []
CACHE = []

dirs = os.listdir('commands')
for file in dirs:
    if file.endswith('.py') and file != '__init__.py':
        command = file[:-3]
        CALLOUTS.append(command.upper())


def completer(text='', idx=0):
    text_lower = text.lower()

    matches = [c for c in (CACHE if CACHE else CALLOUTS) if c.lower().startswith(text_lower)]
    return matches[idx] if idx < len(matches) else None


readline.set_completer(completer)

if readline.__doc__ and "libedit" in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")