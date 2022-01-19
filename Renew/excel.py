# import xlrd
# from openpyxl import load_workbook
#
#
# def read_xls(file):
#     # 实例化excel
#     book = xlrd.open_workbook(file)
#     # 下标读取sheet
#     sheet = book.sheet_by_index(1)
#     # sheet name读取sheet
#     # sheet = book.sheet_by_name('Sheet1')
#     # 获取总行数
#     nrows = sheet.nrows
#     # 循环读取每行数据
#     datas = []
#     for i in range(1, nrows):
#         # print(sheet.row_values(i))
#         # 数据组装dic+t格式
#         data = dict(zip(sheet.row_values(0), sheet.row_values(i)))
#         datas.append(data)
#     return datas
#
#
# def read_xlsx(file):
#     # 加载文件
#     book = load_workbook(file)
#     # sheet name获取sheet：
#     sheet = book['sheet1']
#     # 获取总行数
#     rows = sheet.max_row
#     # 获取总列数
#     # cols = sheet.max_column
#     # print(rows)
#     # 获取表头
#     head = [row for row in sheet.iter_rows(min_row=1, max_row=1, values_only=True)][0]
#     # 数据组装
#     datas = []
#     for row in sheet.iter_rows(min_row=2, max_row=rows + 1, values_only=True):
#         data = dict(zip(head, row))
#         datas.append(data)
#     # print(datas)
#     return datas
#     # 获取单元格值：
#     # Data = sheet.cell(row=row, column=col).value  # 获取表格内容，是从第一行第一列是从1开始的，注意不要丢掉 .value
#
#
# def read_excel(file: str):
#     if file.endswith('xls'):
#         data = read_xls(file)
#     elif file.endswith('xlsx'):
#         data = read_xlsx(file)
#     else:
#         data = ['not support file']
#     return data


# read_xlsx('D:/Desktop/vv.xlsx')


def add(a, b):
    c = a + b
    return c


print(add(4, 5))
