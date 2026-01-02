import sys

def info():
    return '"EXIT" - Exits the application'

def main(state, i):
    conn = state["conn"]
    conn.commit()
    conn.close()
    state["running"] = False

