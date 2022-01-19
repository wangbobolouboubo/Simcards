import xlsxwriter

xl = xlsxwriter.Workbook(r'D:\testfile\卡导入模板py生成.xlsx')
sheet = xl.add_worksheet('模板')
sheet.write_string(0, 0, '卡号')
sheet.write_string(0, 1, 'ICCID')
sheet.write_string(0, 2, '是否注销')
xl.close()

