from DBAssistant import DBAssistant
from DocumentFinder import DocumentFinder
from ParserXml import ParserXml

db_assistant = DBAssistant()
db_assistant.clear_db()

document_finder = DocumentFinder()
file_path = document_finder.find_xml()

parser_xml = ParserXml()
for path in file_path:
    all_kbk = parser_xml.parse(path)

desired_kbk = input()

kbk_len = db_assistant.we_contains_kbk(desired_kbk)

if len(kbk_len) != 0:
    data = db_assistant.select_data(desired_kbk)
    list_len = len(data)
    if list_len != 0:
        print('\n'.join(map(str, data)))
    else:
        print('В данном КБК не проводились операции по кредиту ')
else:
    print('Данного КБК нет в базе данных')



# path = 'C:\\Users\\zohav\\OneDrive\\Desktop\\Finish\\IU_VO_1.xml'

