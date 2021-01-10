#Modules
import requests
import json
import os
import os.path
import zipfile
import shutil

#Tkinter
from tkinter import ttk, Button, Label, Entry, Tk, Menu, filedialog, messagebox
from tkinter import *
import tkinter
from tkinter.ttk import *

#API
req = requests.get("https://api.crafterpika.ml/v1/dwifte.php")
dwpy_api = req.json()

print("Checking if Python Runtime is Extrated")
if os.path.exists(f"./runtime/3.9.0/python.exe"):
    print("Python Runtime Found, Skipping!")
    pass
else:
    print("Python Runtime is not Found!")
    print("Downloading Python Runtime")
    os.mkdir("./runtime/")
    os.mkdir("./runtime/3.9.0")
    pyrdl = requests.get(dwpy_api['runtime'])
    with open(f"./runtime.zip", "wb") as f:
        f.write(pyrdl.content)
    with zipfile.ZipFile(f"./runtime.zip", 'r') as zip_ref:
        zip_ref.extractall(f"./runtime/3.9.0/")
    os.remove(f"./runtime.zip")

print("Installing Requirements")
os.system(f"{os.getcwd()}/runtime/3.9.0/python.exe -m pip install --upgrade pip --no-warn-script-location")
os.system(f"{os.getcwd()}/runtime/3.9.0/python.exe -m pip install -r requirements.txt --no-warn-script-location")

print("Downloading Latest Dwifte.py")
if os.path.exists(f"./dwifte_py/config.json"):
    shutil.copy("./dwifte_py/config.json", f"{os.getcwd()}/config_back_up.json")
else:
    pass
try:
    os.mkdir("./dwifte_py")
except:
    shutil.rmtree("./dwifte_py")
    os.mkdir("./dwifte_py")

dwpydl = requests.get(dwpy_api['download'])
with open(f"./dwifte.zip", "wb") as f:
    f.write(dwpydl.content)
with zipfile.ZipFile(f"./dwifte.zip", 'r') as zip_ref:
    zip_ref.extractall(f"./dwifte_py/")

os.remove("./dwifte.zip")
if os.path.exists(f"{os.getcwd()}/config_back_up.json"):
    os.remove("./dwifte_py/config.json")
    shutil.move(f"{os.getcwd()}/config_back_up.json", f"./dwifte_py/config.json")
else:
    pass