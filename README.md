<p align="center">
  <img src="sqterm/extras/logo2.png" alt="SQTerm Logo" width="170">
</p>

# 

**SQTerm** is a fast, modular, lightweight, terminal SQLite tool written in Python.  
Built for when you don’t want a bloated GUI and just need to get work done — fast.

---

## 🚀 Features

- 🔹 Execute raw SQL commands directly
- 🔹 Clean table output with `tabulate`
- 🔹 Import large CSV files into tables (fast, petl-backed)
- 🔹 Export entire tables or query results to CSV
- 🔹 View tables and their structure
- 🔹 Show simple database statistics
- 🔹 Switch between `.db` files mid-session
- 🔹 Error handling with clear messages
- 🔹 Remove any unused feature by simply deleting a single file
- 🔹 Write your own feature easily in a simple format when preinstalled features don't meet your needs

Tested on tables and `.csv` files with up to **10 million rows**. No problem.

---

## ⬇️ Installation

pip:

`pip install sqterm`

pipx:

`pipx install sqterm`

---

## 🔧 Making your own commands

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

---

## 🛠 Requirements for running source code

- Python 3.x  
- Libraries:  
  - `petl`
  - `sqlalchemy`
  - `tabulate`  
  - `psutil`

Install them with:

```bash
pip install petl sqlalchemy tabulate psutil
