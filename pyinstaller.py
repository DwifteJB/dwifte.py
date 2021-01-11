import shutil
import os
from py7zip import compress

os.system("pyinstaller main.py")
shutil.copy("requirements.txt", "./dist/main/")

file = compress()
file.archive_folder("dist/main", "dwifte_py_launcher_beta")

folders = ["dist", "build", "__pycache__"]
for foldername in folders:
    shutil.rmtree(foldername)

files = ["main.spec"]
for filename in files:
    os.remove(filename)