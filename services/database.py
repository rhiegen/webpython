import sqlite3
from sqlite3 import Error


class db_class:
    def __init__(self):
        self.conn = ""
        self.cursor = ""
        self.sql = ""

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def create_connection_memory(self):
        """ create a database connection to a database that resides
            in the memory
        """
        try:
            self.conn = sqlite3.connect(':memory:')
            print(sqlite3.version)
        except Error as e:
            print(e)

    def create_table(self):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(self.sql)
        except Error as e:
            print(e)
        finally:
            return True

    def close_connection(self):
        self.conn.close()