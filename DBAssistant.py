import sqlite3


class DBAssistant:
    def __init__(self):
        with sqlite3.connect('DB/credit_data.db') as db:
            cursor = db.cursor()
            self.db = db
            self.cursor = cursor
            self.sql_executor(""" CREATE TABLE IF NOT EXISTS kbk_info(KbkId INTEGER, Kbk TEXT, CreditSum INTEGER) """)
            self.sql_executor(""" CREATE TABLE IF NOT EXISTS date_credits(KbkId INTEGER, Credit INTEGER, DateCredit TEXT) """)
            self.clear_table('kbk_info')
            self.clear_table('date_credits')

    def sql_executor(self, query):
        self.cursor.execute(query)
        self.db.commit()
        answer = self.cursor.fetchall()
        return answer

    def insert_kbk(self, kbk_id, kbk, credit_sum):
        query = f""" INSERT INTO kbk_info(KbkId, Kbk, CreditSum) VALUES({kbk_id}, '{kbk}', {round(credit_sum)}) """
        self.sql_executor(query)

    def insert_credit_and_date(self, kbk_id, credit, data_k):
        query = f""" INSERT INTO date_credits(KbkId, Credit, DateCredit) VALUES({kbk_id}, {credit}, '{data_k}') """
        self.sql_executor(query)

    def clear_table(self, table_name):
        query = f""" DELETE FROM {table_name} """
        self.sql_executor(query)

    def get_credit_information(self, kbk_info):
        query = f""" SELECT Credit, DateCredit FROM date_credits WHERE KbkId = {kbk_info} """
        return self.sql_executor(query)

