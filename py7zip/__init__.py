import os
import subprocess
import shlex

"""
**7zip is not created by me. 7zip belongs to Igor Pavlov**

py7zip

Compress/Extract files ot .7z
"""

__version__ = "1.0"
__author__ = 'CrafterPika'
__credits__ = 'https://www.7-zip.org/, Igor Pavlov'


class compress():

    #initial def
    def __init__(self):
        pass

    # make_archive
    def archive_file(self, file, name, password = None):
        module_path = os.path.dirname(__file__)
        cli7z = f"{module_path}/bin/7z.exe"
        if password == None:
            subprocess.run(shlex.split(f'"{cli7z}" a -t7z "{os.getcwd()}/{name}.7z" "{os.getcwd()}/{file}" -mx=9 -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(shlex.split(f'"{cli7z}" a -t7z "-p{password}" "{os.getcwd()}/{name}.7z" "{os.getcwd()}/{file}" -mx=9 -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # folder archiving
    def archive_folder(self, folder, name, password = None):
        module_path = os.path.dirname(__file__)
        cli7z = f"{module_path}/bin/7z.exe"
        if password == None:
            subprocess.run(shlex.split(f'"{cli7z}" a -t7z "{os.getcwd()}/{name}.7z" "{os.getcwd()}/{folder}/*" -mx=9 -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(shlex.split(f'"{cli7z}" a -t7z "-p{password}" "{os.getcwd()}/{name}.7z" "{os.getcwd()}/{folder}/*" -mx=9 -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

class extract():

    #initial def
    def __init__(self):
        pass

    # extract to root folder
    def extract(self, file, password = None):
        module_path = os.path.dirname(__file__)
        cli7z = f"{module_path}/bin/7z.exe"
        if password == None:
            subprocess.run(shlex.split(f'"{cli7z}" e "{os.getcwd()}/{file}.7z" -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(shlex.split(f'"{cli7z}" e "-p{password}" "{os.getcwd()}/{file}.7z" -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # extract to folder name
    def extract_folder(self, file, name, password = None):
        module_path = os.path.dirname(__file__)
        cli7z = f"{module_path}/bin/7z.exe"
        if password == None:
            subprocess.run(shlex.split(f'"{cli7z}" e "{os.getcwd()}/{file}.7z" "-o{os.getcwd()}/{name}" -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(shlex.split(f'"{cli7z}" e "-p{password}" "{os.getcwd()}/{file}.7z" "-o{os.getcwd()}/{name}" -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

class sfx():

    #initial def
    def __init__(self):
        pass

    def creat(self, folder, name):
        module_path = os.path.dirname(__file__)
        cli7z = f"{module_path}/bin/7z.exe"
        subprocess.run(shlex.split(f'"{cli7z}" a -t7z -mx5 -sfx "{name}.exe" "{os.getcwd()}/{folder}/*" -mx=9 -y'), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)