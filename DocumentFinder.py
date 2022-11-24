import os
import shutil
from tkinter import filedialog
from pathlib import Path


class DocumentFinder:
    def find_xml(self):
        file_destination = filedialog.askdirectory()
        file_source = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Start\\'
        get_files = os.listdir(file_source)
        path_to_file = []
        for file_name in get_files:
            if file_name[-4:] == ".xml":
                # shutil.move(file_source + file_name, file_destination)
                shutil.copy(file_source + file_name, file_destination)   # упращение
                path_connector = Path(file_destination, file_name)
                pop = str(path_connector.resolve())
                path_to_file.append(pop)
        return path_to_file
