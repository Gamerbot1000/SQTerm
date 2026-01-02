<p align="center">
  <img src="extras/logo2.png" alt="SQTerm Logo" width="170">
</p>

# 

**SQTerm** is a fast, lightweight, terminal-based SQLite tool written in Python.  
Built for when you don’t want a bloated GUI and just need to get work done — fast.

---

## 🚀 Features

- 🔹 Execute raw SQL commands directly
- 🔹 Clean table output with `tabulate`
- 🔹 TUI for browsing and editing tables (`VISUALEDIT`)
- 🔹 Import large CSV files into tables (fast, petl-backed)
- 🔹 Export entire tables or query results to CSV
- 🔹 View tables and their structure
- 🔹 Show simple database statistics
- 🔹 Switch between `.db` files mid-session
- 🔹 Error handling with clear messages

Tested on tables and `.csv` files with up to **10 million rows**. No problem.

---

## 🛠 Requirements for running code

- Python 3.x  
- Libraries:  
  - `petl`
  - `sqlalchemy`
  - `tabulate`  
  - `psutil`
  - `keyboard`

Install them with:

```bash
pip install petl sqlalchemy tabulate psutil keyboard
