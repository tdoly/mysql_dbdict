#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2013-12-23

@author: mingdong.li

excel option
xlrd : reading data and formatting information from Excel files
xlwt : writing data and formatting information to Excel files
xlutils : both xlrd and xlwt
'''
from xlrd import open_workbook
from xlwt import Workbook,easyxf
from xlutils.copy import copy

class ExcelTemplateUtils():
    '''
    excel template utils
    '''
    
    def __init__(self, filename):
        self.filename = filename
        self.wb = self.getWB()
        
    def getWB(self):
        '''get the workbook'''
        rb = open_workbook(self.filename, formatting_info=True)
        wb = copy(rb)
        return wb
    
    def add(self, rowCount, lineCount, value, sheetCount):
        '''
        @param rowCount: 行号
        @param lineCount: 列号
        @param value: cell的值
        @param sheetCount: sheet号
        @param wb: wb
        '''
        self.wb.get_sheet(sheetCount).write(rowCount, lineCount, value)
    
    def save(self):
        self.wb.save(self.filename)
        

class ExcelNoTemplateUtils():
    
    def __init__(self, filename):
        self.filename = filename
        self.book = Workbook()
    
    def ezxf(self, xf=""):
        return easyxf(xf)
    
    def addSheet(self, sheet_name):
        return self.book.add_sheet(sheet_name)
    
    def write(self, sheet, headings, data, heading_xf=easyxf(), title_xf=easyxf(), data_xfs=easyxf(), rowx=0):
        '''
        @param sheet_name: excel sheet
        @param headings: the first row in the sheet
        @type data: dict
        @param heading_xf: style
        @param data_xfs: style
        @param title_xf: style
        @param rowx: row
        
        Example:
        heading_xf=xlwt.ezxf('font: bold on; align: wrap on, vert centre, horiz center')
        '''
        maxCol = 0
        for colx, value in enumerate(headings):
            sheet.write(rowx, colx, value, heading_xf)
            maxCol = colx
        
        sheet.set_panes_frozen(True) # frozen headings instead of split panes
        sheet.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
        sheet.set_remove_splits(True) # if user does unfreeze, don't leave a split there
        
        for k,v in data.iteritems():
            '''
            Usage:
            {'two': 
             [['ID', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'one ID'],
             ['NAME', 'varchar(128)', 'NO', '', 'NULL', '', ''], 
             ['DATE', 'datetime', 'NO', '', 'NULL', '', '']], 
             'one': 
             [['ID', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'one ID'], 
             ['NAME', 'varchar(128)', 'NO', '', 'NULL', '', ''], 
             ['DATE', 'datetime', 'NO', '', 'NULL', '', '']]}
            '''
            rowx += 1
            sheet.write_merge(rowx, rowx, 0, maxCol, k, title_xf)
            for row in v:
                rowx += 1
                for colx, value in enumerate(row):
                    sheet.write(rowx, colx, value, data_xfs)
            rowx += 1
        
        return rowx
    
    def save(self):
        self.book.save(self.filename)