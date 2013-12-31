#!/usr/bin/env python
#-*- coding: utf-8 -*-

from mysql_dbdict.client import DictClient
import logging
client = DictClient("localhost")
#logging.error(client.get("conn"))
#logging.error(client.get("ignore_db"))

#cursor = conn.get("conn").cursor()
logging.error(client.execute("use wml_db"))
logging.error(client.execute("select USERNAME from information_schema.user"))

rows = client.execute("show tables")
for row in rows:
    print row

rows = client.execute("desc user")
for row in rows:
    print row