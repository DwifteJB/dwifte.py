#Modules
import requests
import json
import os
import os.path
import zipfile
import shutil
import threading

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

def token_save():
    with open("./dwifte_py/config.json") as f:
        config = json.load(f)
    token_input = token.get()
    config["token"] = f"{token_input}"
    with open(f'./dwifte_py/config.json', 'w') as f:
        json.dump(config, f, indent=4)

def prefix_save():
    with open("./dwifte_py/config.json") as f:
        config = json.load(f)
    prefix_input = prefix.get()
    config["prefix"] = f"{prefix_input}"
    with open(f'./dwifte_py/config.json', 'w') as f:
        json.dump(config, f, indent=4)

def run_dwpy():
    og = os.getcwd()
    os.chdir(f"{os.getcwd()}/dwifte_py")
    os.system(f"{og}/runtime/3.9.0/python.exe main.py")

def run():
    thread1 = threading.Thread(target=run_dwpy)
    thread1.start()

main = Tk()
main.title("Dwifte.PY Launcher (Beta)")
main.geometry("500x490")

title = Label(main, text="Dwifte.PY Launcher (Beta)")
title.pack()
empty = Label(main)
empty.pack()
empty1 = Label(main)
empty1.pack()

token1 = Label(main, text="Token:")
token1.pack()
token = ttk.Entry(main)
token.pack()
save_token = ttk.Button(main, text="Save to Configuration", command=token_save)
save_token.pack()
empty2 = Label(main)
empty2.pack()
empty3 = Label(main)
empty3.pack()
prefix1 = Label(main, text="Prefix:")
prefix1.pack()
prefix = ttk.Entry(main)
prefix.pack()
save_prefix = ttk.Button(main, text="Save to Configuration", command=prefix_save)
save_prefix.pack()
empty4 = Label(main)
empty4.pack()
run = ttk.Button(main, text="Run Dwifte.py", command=run)
run.pack()


main.mainloop()