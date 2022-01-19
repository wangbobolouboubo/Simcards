import xlsxwriter

xl = xlsxwriter.Workbook(r'D:\testfile\导入.xlsx')
sheet = xl.add_worksheet()
# sheet.write_string(0, 0, '卡号')
# sheet.write_string(0, 1, 'ICCID')
# sheet.write_string(0, 2, '是否注销')
# # writer_string(a,b,v) 参数 第一个参数是行 第二个参数是列 第三个参数是单元格的值


# 卡号
card_no = 89812604000
# 对应iccid
ICCID = 444489812604000

# 0,1 (0,第一次导入，1第二次导出)
is_import = 1
# 位置第几行
location = 0
if card_no < 89812605000:
    for i in range(0, 1000):
        card_no = card_no + 1
        ICCID = ICCID + 1
        for j in range(0, 1):
            location = location + 1
        sheet.write_number(location, 0, card_no)
        sheet.write_number(location, 1, ICCID)
        sheet.write_number(location, 2, is_import)

xl.close()


# 这个只能新建文件 不能对已有的文件进行写入/更新
