'''
Created on 2013-12-30

@author: mingdong.li

select data
'''

from client import DictClient
import zerorpc

class DbData(object):
    def __init__(self, dbname):
        self.client = DictClient(dbname)

    def getDB(self):
        result = [database[0] for database in self.client.execute("show databases")]
        if result:
            for ignore in ["information_schema", "mysql", "performance_schema"]:
                result.remove(ignore)
        return result

    def getTable(self, database):
        if database:
            self.client.execute("use %s" % database)
            return [tables[0] for tables in self.client.execute("show tables")]

    def getColumn(self, table):
        if table:
            return [list(column) for column in self.client.execute("desc %s" % table)]

    def getDatas(self, sheet):
        datas = {}
        if sheet:
            tables = self.getTable(sheet)
            if tables:
                for table in tables:
                    columns = self.getColumn(table)
                    datas[table] = columns
        return datas

server = zerorpc.Server(DbData("localhost"))
server.bind("tcp://0.0.0.0:4242")
server.run()

