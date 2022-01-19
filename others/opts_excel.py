'''写入excel文件'''
import xlsxwriter

# todo 创建excel文件
xl = xlsxwriter.Workbook(r'D:\testfile\testt10.xlsx')

# todo 添加sheet
sheet = xl.add_worksheet('自增1112')

# todo 往单元格cell添加数据,索引写入
sheet.write_string(0, 0, '卡号')

# todo 位置写入
sheet.write_string('B1', 'ICCID')
# 卡号
a = 89812604000
# 对应iccid
b = 444489812604000
# 设置行的索引location=0 第一行
location = 0
if a < 89812605000:
    for i in range(0, 1000):
        a = a + 1
        b = b + 1
        for j in range(0, 1):
            location = location + 1
            # sheet.write_string(0, location, a)
        sheet.write_number(location, 0, a)
        sheet.write_number(location, 1, b)
        print(a, 'a最终')
        print(b, 'b最终')
        print(location, 'location最终')

# todo 设置单元格宽度大小
sheet.set_column('A:B', 30)

# todo 关闭文件
xl.close()





