from DBAssistant import DBAssistant
from DocumentFinder import DocumentFinder
from ParserXml import ParserXml

db_assistant = DBAssistant()
db_assistant.clear_db()

document_finder = DocumentFinder()
file_path = document_finder.find_xml()

parser_xml = ParserXml()
for path in file_path:
    parser_xml.parse(path)

desired_kbk = input()

if not db_assistant.is_new_kbk(desired_kbk):
    data = db_assistant.select_data(desired_kbk)
    if len(data):
        print('\n'.join(map(str, data)))
    else:
        print('В данном КБК не проводились операции по кредиту')
else:
    print('Данного КБК нет в базе данных')
