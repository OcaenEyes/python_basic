# 读取Excel
import xlrd
# 写入excel
import xlwt

xlsx = xlrd.open_workbook("../datasource/7月下旬入库表.xlsx")
table = xlsx.sheet_by_index(0)
print(table.cell_value(1,4))

new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet("new_sheet")
worksheet.write(0,0,"testSheet")
new_workbook.save("../datasource/text-save.xls")
