import os
import shutil
from os import path
from tkinter import filedialog
import pathlib
from pathlib import Path


path_save = filedialog.askdirectory(initialdir=path)

FILE_SOURCE = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Start\\'
file_destination = path_save
get_files = os.listdir(FILE_SOURCE)

for file_name in get_files:
    if file_name[-4:] == ".xml":
        shutil.move(FILE_SOURCE + file_name, file_destination)

        # file_path = pathlib.Path.home() (полезная штука, надо разобраться с ней)
        # file_path = pathlib.Path.cwd() (полезная штука, надо разобраться с ней)

        path = Path(path_save, file_name)
        print(str(path))
















# разархировка файла

# import zipfile
# file_zip = zipfile.ZipFile('C:\\Users\\zohav\\OneDrive\\Desktop\\SS\\DD.zip')
# file_zip.extractall('C:\\Users\\zohav\\OneDrive\\Desktop\\SS\\')
# file_zip.close()
# path = os.path.join(os.path.abspath(os.path.dirname(directory_path + "/")), name_file)
# os.remove(path)
