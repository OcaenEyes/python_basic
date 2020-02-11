import xlwt
import xlrd
import pyecharts
from xlutils.copy import copy

xlsx = xlrd.open_workbook("../datasource/7月下旬入库表.xlsx")
table = xlsx.sheet_by_index(0)

all_data = []
for n in range(1, table.nrows):
    company = table.cell_value(n, 1)
    price = table.cell_value(n, 3)
    weight = table.cell_value(n, 4)

    data = {'company': company, 'weight': weight, 'price': price}
    all_data.append(data)


print(all_data)
