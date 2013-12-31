#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

"""
the arguments use to create a connetcion to the database.

    "host": host to connect
    "user": user to connect as
    "passwd": password to user
    "db": database to use
    "port": TCP/IP port to connect to, default port is 3306
    "charset": # If supplied, the connection character set will be changed to this character set
    "use_unicode": If True, text-like columns are returned as unicode objects using the connection's character set.Otherwise, text-like columns are returned as strings.
    "ignore_db": set the name of database and you don't want to generate the database dictionary
"""
OPTIONS = {
    "localhost": {
        "host": "localhost",
        "user": "testuser",
        "passwd": "testpwd",
        "db": "",
        "port": 3306,
        "charset": "utf8",
        "use_unicode": False,
        "ignore_db": ["information_schema", "mysql", "performance_schema"]
    }
}


class DictClient(object):

    """docstring for Client"""

    def __init__(self, arg=None):
        self.arg = arg
        self.con = DictClient.conn(self)['conn']
        self.ignore = DictClient.conn(self)['ignore_db']
        

    def conn(self):
        settings = OPTIONS.get(self.arg)
        result = {}
        
        if not settings:
            raise "the options is error"
        
        host = settings.get("host")
        user = settings.get("user")
        passwd = settings.get("passwd")
        db = settings.get("db")
        port = settings.get("port")
        charset = settings.get("charset")
        use_unicode = settings.get("use_unicode")
        ignore_db = settings.get("ignore_db")

        conn = MySQLdb.connect(
            host=host, user=user, passwd=passwd, db=db, port=port, charset=charset, use_unicode=use_unicode)

        if conn:
            result["conn"] = conn
        if ignore_db:
            result["ignore_db"] = ignore_db
        return result
    
    def cursor(self):
        return self.con.cursor()
    
    def execute(self, query, args=None):
#        try:
#            with self.con:
#                cur = self.con.cursor()
#                for ig in self.ignore:
#                    if ig in query:
#                        return None
#                cur.execute(query, args)
#                rows = cur.fetchall()
#                return rows
#        except:
        cur = DictClient.cursor(self)
        for ig in self.ignore:
            if ig in query:
                raise 'No support this database'
        cur.execute(query, args)
        rows = cur.fetchall()
        return rows

    def close(self):
        if self.con:
            self.con.close()
        if self.cur:
            self.cur.close()
