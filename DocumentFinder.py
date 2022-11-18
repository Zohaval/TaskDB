import os
import shutil
from tkinter import filedialog
from pathlib import Path


class DocumentFinder:
    def find_xml(self):
        file_destination = filedialog.askdirectory()
        file_source = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Start\\'
        get_files = os.listdir(file_source)
        for file_name in get_files:
            if file_name[-4:] == ".xml":
                shutil.move(file_source + file_name, file_destination)
                path_to_file = Path(file_destination, file_name)
                return path_to_file
