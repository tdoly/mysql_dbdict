#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: export_excel.py
Author: tdoly
Description: export excel
'''
from excel_util import ExcelNoTemplateUtils
import rpc_client as rc

def export():
    entu = ExcelNoTemplateUtils('dbdict.xls')
    heading_xf = entu.ezxf('font: bold on; align: wrap off, vert centre, horiz center')
    title_xf = entu.ezxf('font: bold on, color blue; align: wrap on, vert bottom, horiz center; border: left thin, right thin, top thin, bottom thin')
    data_xfs = entu.ezxf('font: bold off; align: wrap off, vert centre, horiz left; border: left thin, right thin, top thin, bottom thin')

    headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
    sheets = rc.dbs() # 每个数据库作为一个sheet表格
    datas = {}
    for sheet in sheets:
        datas = rc.datas(sheet)
        sheet = entu.addSheet(sheet)
        entu.write(sheet, headings, datas, heading_xf, title_xf, data_xfs)

    entu.save()

if __name__ == '__main__':
    print "==export start=="
    export()
    print "==End=="
