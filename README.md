<p align="center">
  <img src="extras/logo2.png" alt="SQTerm Logo" width="170">
</p>

# 

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
- 🔹 Show simple database statistics
- 🔹 Error handling with clear messages

Tested on tables and `.csv` with up to **10 million rows**. No problem.

---

## 🛠 Requirements

- Python 3.x  
- Libraries:  
  - `pandas`  
  - `tabulate`  
  - `psutil`
  - `threading`

Dependencies to install if you wish to run the code yourself:

```bash
pip install pandas tabulate psutil threading

