# _*_ coding:utf-8 _*_
import openpyxl
def get_excel():
    book = openpyxl.load_workbook('./data.xlsx')
    sheet = book.get_sheet_by_name("密钥")
    values = []
    for row in sheet:
        lines = []
        for cell in row:
            lines.append(cell.value)
        values.append(lines)
    print(values)
    return values