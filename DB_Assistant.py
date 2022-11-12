import sqlite3


class DB_Assistant:
    def __init__(self):
        with sqlite3.connect('DB/credit_data.db') as db:
            cursor = db.cursor()
            self.db = db
            self.cursor = cursor
            self.execute_order_66(""" CREATE TABLE IF NOT EXISTS tags_xml(КБК_id INTEGER, КБК TEXT, СуммаК INTEGER) """)
            self.execute_order_66(""" CREATE TABLE IF NOT EXISTS tags_xml2(КБК_id INTEGER, Кредит INTEGER, Дата_к TEXT) """)
            self.clear_table('tags_xml')
            self.clear_table('tags_xml2')

    def execute_order_66(self, query):
        self.cursor.execute(query)
        self.db.commit()
        answer = self.cursor.fetchall()
        return answer

    def insert(self, kbk_id, kbk, sum_kredita):
        query = f""" INSERT INTO tags_xml(КБК_id, КБК, СуммаК) VALUES({kbk_id}, '{kbk}', {round(sum_kredita)}) """
        self.execute_order_66(query)

    def insert2(self, kbk_id, kredit, data_k):
        query = f""" INSERT INTO tags_xml2(КБК_id, Кредит, Дата_к) VALUES({kbk_id}, {kredit}, '{data_k}') """
        self.execute_order_66(query)

    def clear_table(self, table_name):
        query = f""" DELETE FROM {table_name} """
        self.execute_order_66(query)

    def get(self, kbk_info):
        query = f""" SELECT Кредит, Дата_к FROM tags_xml2 WHERE КБК_id = {kbk_info} """
        return self.execute_order_66(query)

