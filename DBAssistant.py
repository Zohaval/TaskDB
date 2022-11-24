import sqlite3


class DBAssistant:
    def __init__(self):
        with sqlite3.connect('DB/credit_data.db') as db:
            cursor = db.cursor()
            self.db = db
            self.cursor = cursor
            self.sql_executor(""" CREATE TABLE IF NOT EXISTS kbk_info(Kbk TEXT, CreditSum INTEGER) """)
            self.sql_executor(""" CREATE TABLE IF NOT EXISTS date_credits(Kbk TEXT, Credit INTEGER, DateCredit TEXT) """)

    def sql_executor(self, query):
        self.cursor.execute(query)
        self.db.commit()
        answer = self.cursor.fetchall()
        return answer

    def insert_kbk(self, kbk, credit_sum):
        query = f""" INSERT INTO kbk_info(Kbk, CreditSum) VALUES('{kbk}', {round(credit_sum)}) """
        self.sql_executor(query)

    def insert_credit_and_date(self, kbk, credit, data_k):
        query = f""" INSERT INTO date_credits(Kbk, Credit, DateCredit) VALUES('{kbk}', {credit}, '{data_k}') """
        self.sql_executor(query)

    def clear_table(self, table_name):
        query = f""" DELETE FROM {table_name} """
        self.sql_executor(query)

    def clear_db(self):
        self.clear_table('kbk_info')
        self.clear_table('date_credits')

    def select_data(self, desired_kbk):
        query = f""" SELECT Credit, DateCredit FROM date_credits WHERE Kbk = '{desired_kbk}' """
        return self.sql_executor(query)

    def we_contains_kbk(self, desired_kbk):
        query = f""" SELECT Kbk FROM kbk_info WHERE Kbk = '{desired_kbk}' """
        return self.sql_executor(query)
