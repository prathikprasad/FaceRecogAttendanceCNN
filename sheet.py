import xlwt
import xlrd
from xlutils.copy import copy
import os
import datetime
import xlsxwriter

st_name = 'prathik', 'lata'
def mark_present(st_name):

	names = os.listdir('output')
	print(names)

	dt = str(datetime.date.today())
	sub = dt.replace("-", "_").replace(":", "_").replace(" ", "_")
	sub
	
	if not os.path.exists('attendance/' + sub + '.xls'):
		count = 2
		workbook = xlsxwriter.Workbook('attendance/' + sub + '.xls')
		print("Creating Spreadsheet with Title: " + sub)
		sheet = workbook.add_worksheet() 
		for i in names:
		    sheet.write(count, 0, i)
		    count += 1
		workbook.close() 

	rb = xlrd.open_workbook('attendance/' + sub + '.xls')
	wb = copy(rb)
	sheet = wb.get_sheet(0)
	sheet.write(1,1,str(datetime.datetime.now()))


	count = 2
	for i in names:
	    if i in st_name:
        	sheet.write(count, 1, 'P')
        	sheet.write(count, 2, datetime.datetime.now().strftime("%H:%M"))
	    else:
        	sheet.write(count, 1, 'A')
        	sheet.write(count, 2, datetime.datetime.now().strftime("%H:%M"))
	    sheet.write(count, 0, i)
	    count += 1

	wb.save('attendance/' + sub + '.xls')


mark_present(st_name)
#print(datetime.datetime.now())