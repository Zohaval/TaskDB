import os
import shutil
from os import path
from tkinter import *
from tkinter import filedialog
from pathlib import Path
import sqlite3
from xml.etree.ElementTree import ElementTree
import bs4
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from DB_Assistant import DB_Assistant


file_destination = filedialog.askdirectory(initialdir=path)

FILE_SOURCE = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Start\\'
get_files = os.listdir(FILE_SOURCE)

for file_name in get_files:
    if file_name[-4:] == ".xml":
        shutil.move(FILE_SOURCE + file_name, file_destination)
        PATH = Path(file_destination, file_name)
        # временное решение с PATH

moto = DB_Assistant()
tree: ElementTree = ET.parse(PATH)
root = tree.getroot()
kbk_id = 0
for payment in root.iter('ВыпОперРСБ'):
    kbk = payment.attrib.get('КБК')
    kbk_id += 1
    sum_kredita = 0
    list_operations = payment.findall('ЗапОперРСБ')
    for operation in list_operations:
        summa = operation.find('Сумма')
        data = operation.find('ДокОтч')
        if summa is not None:
            kredit = summa.attrib.get('Кредит')
            data_k = data.attrib.get('ДатаПредстДО')
            if kredit is not None:
                sum_kredita = sum_kredita + float(kredit)
                moto.insert2(kbk_id, float(kredit), data_k)
    moto.insert(kbk_id, kbk, sum_kredita)

kbk_info = int(input())

if kbk_info <= kbk_id:
    data = moto.get(kbk_info)
    list_len = len(data)
    if list_len != 0:
        print('\n'.join(map(str, data)))
    else:
        print('В данном КБК не проводились операции по кредиту ')
else:
    print('Данного КБК нет в базе данных')

