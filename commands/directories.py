import os

def dir():

    databases_dir = os.path.join(os.path.dirname(__file__), "databases")
    exports_dir = os.path.join(os.path.dirname(__file__), "exports")

    print(f"Databases Directory: {databases_dir}")
    print(f"Exports Directory: {exports_dir}")