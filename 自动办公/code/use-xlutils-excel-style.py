import xlwt
import xlutils
import xlrd
from xlutils.copy import copy

test_excel = xlrd.open_workbook("../datasource/日统计.xls", formatting_info=True)
test_sheet = test_excel.sheet_by_index(0)

new_excel = copy(test_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()
font = xlwt.Font()
font.name = "微软雅黑"
font.bold = True
font.height = 360
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

new_sheet.write(2, 1, 12, style)
new_sheet.write(3, 1, 16, style)
new_sheet.write(4, 1, 18, style)
new_sheet.write(5, 1, 19, style)
new_sheet.write(5, 1, 19, style)

new_excel.save("../datasource/write-excel-style.xls")
