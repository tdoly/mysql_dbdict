#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2013-12-23

@author: mingdong.li
'''

from mysql_dbdict.excel_util import ExcelNoTemplateUtils,ExcelTemplateUtils

def test_no_template():
    entu = ExcelNoTemplateUtils('E:/one.xls')
    heading_xf = entu.ezxf('font: bold on; align: wrap off, vert centre, horiz center')
    title_xf = entu.ezxf('font: bold on, color blue; align: wrap off, vert centre, horiz center; border: left thin, right thin, top thin, bottom thin')
    data_xfs = entu.ezxf('font: bold off; align: wrap off, vert centre, horiz center; border: left thin, right thin, top thin, bottom thin')
    
    dbs = ['test', 'one', 'two']
    headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra', 'Comment']
    
    table = ['one', 'two']
    data = [['ID', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'one ID'],
            ['NAME', 'varchar(128)', 'NO', '', 'NULL', '', ''],
            ['DATE', 'datetime', 'NO', '', 'NULL', '', '']
            ]
    datas = {}
    for title in table:
        datas[title] = data
    for db in dbs:
        sheet = entu.addSheet(db)
        entu.write(sheet, headings, datas, heading_xf, title_xf, data_xfs)
    entu.save()
    
test_no_template()