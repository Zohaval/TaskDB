import os
import shutil
from os import path
from tkinter import filedialog
from pathlib import Path
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
from DBAssistant import DBAssistant


file_destination = filedialog.askdirectory(initialdir=path)

FILE_SOURCE = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Start\\'
get_files = os.listdir(FILE_SOURCE)

db_assistant = DBAssistant()
tree: ElementTree = ET.parse(PATH)
root = tree.getroot()
kbk_id = 0
for payment in root.iter('ВыпОперРСБ'):
    kbk = payment.attrib.get('КБК')
    kbk_id += 1
    credit_sum = 0
    list_operations = payment.findall('ЗапОперРСБ')
    for operation in list_operations:
        summa = operation.find('Сумма')
        data = operation.find('ДокОтч')
        if summa is not None:
            credit = summa.attrib.get('Кредит')
            date = data.attrib.get('ДатаПредстДО')
            if credit is not None:
                credit_sum = credit_sum + float(credit)
                db_assistant.insert_credit_and_date(kbk_id, float(credit), date)
    db_assistant.insert_kbk(kbk_id, kbk, credit_sum)

kbk_info = int(input())

if kbk_info <= kbk_id:
    data = db_assistant.get_credit_information(kbk_info)
    list_len = len(data)
    if list_len != 0:
        print('\n'.join(map(str, data)))
    else:
        print('В данном КБК не проводились операции по кредиту ')
else:
    print('Данного КБК нет в базе данных')

