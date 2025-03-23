# SQTerm

**SQTerm** is a fast, lightweight, terminal-based SQLite tool written in Python.  
Built for when you don’t want a bloated GUI and just need to get work done—fast.

---

## 🚀 Features

- 🔹 Execute raw SQL commands directly
- 🔹 Clean table output with `tabulate`
- 🔹 Import large CSV files into tables (fast, pandas-backed)
- 🔹 Export entire tables or query results to CSV
- 🔹 View tables and their structure
- 🔹 Switch between `.db` files mid-session
- 🔹 Error handling with clear messages

Tested on files with up to **10 million rows**. No problem.

---

## 🛠 Requirements

- Python 3.x  
- Libraries:  
  - `pandas`  
  - `tabulate`  
  - `psutil`
  - `threading`

Install dependencies:

```bash
pip install pandas tabulate psutil threading

