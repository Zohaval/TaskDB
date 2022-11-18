from DBAssistant import DBAssistant
from DocumentFinder import DocumentFinder
from ParserXml import ParserXml


# path = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Finish\\IU_VO_1.xml'

db_assistant = DBAssistant()
db_assistant.clear_db()

document_finder = DocumentFinder()
file_path = document_finder.find_xml()

parser_xml = ParserXml()
kbk_id = parser_xml.parse(file_path)

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
