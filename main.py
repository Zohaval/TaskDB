import os
import zipfile
import shutil
from os import path
from tkinter import filedialog


path_save = filedialog.askdirectory(initialdir='C:\\Users\\zohav\\OneDrive\\Desktop')

file_source = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Start\\'
file_destination = path_save
get_files = os.listdir(file_source)

for g in get_files:
    shutil.move(file_source + g, file_destination)







# разархировка файла
# file_zip = zipfile.ZipFile('C:\\Users\\zohav\\OneDrive\\Desktop\\SS\\DD.zip')
# file_zip.extractall('C:\\Users\\zohav\\OneDrive\\Desktop\\SS\\')
# file_zip.close()
# path = os.path.join(os.path.abspath(os.path.dirname(directory_path + "/")), name_file)
# os.remove(path)
