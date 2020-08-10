import pyodbc

class dbBase(object):
    def __init__(self, dsn):
        self.db = pyodbc.connect(dsn)
        self.cursor = self.db.cursor()

    def check_if_table_exists(self, tableName):
        table_exists_statement = "SELECT COUNT(*) FROM X$File WHERE Xf$Name = '" + tableName + "'"

        table_count = self.cursor.execute(table_exists_statement)
        table_count = table_count.fetchone()[0]

        return table_count == 1