from openpyxl import Workbook, load_workbook

wb = load_workbook("Book1.xlsx")

sh = wb['Sheet1']

print(sh['B2'].value)








