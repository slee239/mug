def save_to_new_excel_workbook(data,workbook_name,worksheet_name):
	import pandas as pd
	writer = pd.ExcelWriter(workbook_name)
	data.to_excel(writer,worksheet_name, index=False)
	writer.save()
	return

def add_worksheet_to_existing_workbook(data, workbook_name, worksheet_name):
	import pandas as pd
	from openpyxl import load_workbook
	book = load_workbook(workbook_name)
	writer = pd.ExcelWriter(workbook_name, engine = 'openpyxl')
	writer.book = book
	data.to_excel(writer,worksheet_name)
	writer.save()
	return

def convert_pickle_to_excel(directory):
	import glob
	import pandas as pd
	data = pd.read_pickle(directory)
	save_to_new_excel_workbook(data,directory.split('.')[0]+'.xlsx','New Worksheet')
	return