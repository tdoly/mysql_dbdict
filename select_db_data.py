'''
Created on 2013-12-30

@author: mingdong.li

select data
'''

from client import DictClient

client = DictClient("localhost")

def getDB():
    result = [database[0] for database in client.execute("show databases")]
    if result:
        for ignore in ["information_schema", "mysql", "performance_schema"]:
            result.remove(ignore)
    return result
    
    
def getTable(database):
    if database:
        client.execute("use %s" % database)
        return [tables[0] for tables in client.execute("show tables")]

def getColumn(table):
    if table:
        return [list(column) for column in client.execute("desc %s" % table)]
#        return client.execute("desc %s" % table)

def getDatas(sheet):
    datas = {}
    if sheet:
        tables = getTable(sheet)
        if tables:
            for table in tables:
                columns = getColumn(table)
                datas[table] = columns
    return datas
