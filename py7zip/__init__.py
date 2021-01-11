import os
import subprocess
import shlex
from dotenv import load_dotenv

load_dotenv()

"""
**7zip is not created by me. 7zip belongs to Igor Pavlov**

py7zip

Compress/Extract files ot .7z
"""

__version__ = "0.1"
__author__ = 'CrafterPika'
__credits__ = 'https://www.7-zip.org/, Igor Pavlov'


class compress():

    #initial def
    def __init__(self):
        pass

    # make_archive
    def archive_file(self, file, name):
        module_path = os.path.dirname(__file__)
        bin = os.getenv("7ZIP_BIN")
        cli7z = f"{module_path}{bin}"
        #print(cli7z)
        subprocess.run(shlex.split(f'"{cli7z}" a -t7z "{os.getcwd()}/{name}.7z" "{os.getcwd()}/{file}" -mx=9'))

    # folder archiving
    def archive_folder(self, folder, name):
        module_path = os.path.dirname(__file__)
        bin = os.getenv("7ZIP_BIN")
        cli7z = f"{module_path}{bin}"
        #print(cli7z)
        subprocess.run(shlex.split(f'"{cli7z}" a -t7z "{os.getcwd()}/{name}.7z" "{os.getcwd()}/{folder}/*" -mx=9'))

class extract():

    #initial def
    def __init__(self):
        pass

    # extract to root folder
    def extract(self, file):
        module_path = os.path.dirname(__file__)
        bin = os.getenv("7ZIP_BIN")
        cli7z = f"{module_path}{bin}"
        subprocess.run(shlex.split(f'"{cli7z}" e "{os.getcwd()}/{file}.7z"'))

    # extract to folder name
    def extract_folder(self, file, name):
        module_path = os.path.dirname(__file__)
        bin = os.getenv("7ZIP_BIN")
        cli7z = f"{module_path}{bin}"
        subprocess.run(shlex.split(f'"{cli7z}" e "{os.getcwd()}/{file}.7z" "-o{os.getcwd()}/{name}"'))