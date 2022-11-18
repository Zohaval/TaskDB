from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
from DBAssistant import DBAssistant

class ParserXml:
    def __init__(self):
        self.db_assistant = DBAssistant()

    def parse(self, file_path):
        tree: ElementTree = ET.parse(file_path)
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
                        self.db_assistant.insert_credit_and_date(kbk_id, float(credit), date)
            self.db_assistant.insert_kbk(kbk_id, kbk, credit_sum)
        return kbk_id
