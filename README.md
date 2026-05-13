
<p align="center">
  <img src="sqterm/extras/newlogo.png" alt="SQTerm Logo" width="300">
</p>

# 

**SQTerm** is a fast, modular, lightweight, terminal SQLite tool written in Python.  
Built for when you don’t want a bloated GUI and just need to get work done — fast.

---

## Features

- Execute raw SQL commands directly
- Clean table output with `tabulate`
- Import CSV files
- Export entire tables to CSV
- View tables and their structure
- Show various database statistics
- Basic autocompletion
- Switch between `.db` files mid-session
- Error handling with clear messages
- Remove any unused feature by simply deleting a single file
- Write your own feature easily in a simple format when preinstalled features don't meet your needs


---

## Installation

pip:

```bash
pip install sqterm
```

pipx:

```bash
pipx install sqterm
```

---

## Making your own commands

To make your own command simply create a .py file titled **exactly** what the user has to type to execute the command.

Each command consists of two required functions:
- `info()` – returns a short description of the command
- `main(state, i)` – contains the command logic

Example of an `info()` function:

```py
def info():
    return '"IMPORTCSV" - Imports a CSV file as a new table'
```

Example of a `main()` function:

```py
def main(state, i):
    print("Hello from this command!")
```

If your script needs access to things such as the database path, the SQLite connection, or the cursor, you can retrieve them from the state argument:

```py
name = state["name"]
conn = state["conn"]
cursor = state["cursor"]
```
If you need the raw user input that triggered the command, you can access it via the i argument passed into main().
Once you've written your command simply drop it into the `commands` folder, start SQTerm and your command should work seamlessly when executed (you can also type `help` to see if your command shows up)

It is recommended to use autocompletion if your addon requires the user to input columns, tables, etc. You can use the built-in autocompletion by importing its `CACHE` variable via:
```py 
from sqterm.extras.autocomplete import CACHE
```

If there's anything you'd like to be autocompleted simply append it to the cache using `CACHE.append(ITEM)`, before the addon finishes also make sure to clear the cache using `CACHE.clear()`.


---

## Requirements for running source code

- Python 3.x  
- Libraries:
  - `prompt_toolkit`
  - `tabulate`  
  - `psutil`

Install them with:

```bash
pip install prompt_toolkit tabulate psutil
