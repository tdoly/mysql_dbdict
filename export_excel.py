
from excel_util import ExcelNoTemplateUtils
from select_db_data import *

def export():
    entu = ExcelNoTemplateUtils('dbdict.xls')
    heading_xf = entu.ezxf('font: bold on; align: wrap off, vert centre, horiz center')
    title_xf = entu.ezxf('font: bold on, color blue; align: wrap on, vert bottom, horiz center; border: left thin, right thin, top thin, bottom thin')
    data_xfs = entu.ezxf('font: bold off; align: wrap off, vert centre, horiz left; border: left thin, right thin, top thin, bottom thin')
    
    
    headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
    dbs = getDB()
    datas = {}
    for db in dbs:
        datas = getDatas(db)
        sheet = entu.addSheet(db)
        entu.write(sheet, headings, datas, heading_xf, title_xf, data_xfs)
    
    entu.save()

if __name__ == '__main__':
    print "==export start=="
    export()
    print "==End=="
