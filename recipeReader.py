from openpyxl import *

wb = load_workbook(filename = 'Pasztet.xlsx')
sheet_ranges = wb['Sheet1']
print(sheet_ranges['B2'].value)
