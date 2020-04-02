import os
import glob
import numpy as np
import pandas as pd
import sys

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 100)

def read_text_files_from_directory():
	txt_file = glob.glob("*.txt")
	if len(txt_file)!=1:
		print("We need to have 1 txt file.")
		print("There are {} txt file(s) in the folder: {}".format(len(txt_file), txt_file))
		print("Try again")
		input("")
		sys.exit()
	else:
		fname = txt_file[0]
		print("Reading {}".format(fname))
	return fname

import textract

def extract_text_from_pdf(fname):
	# try:
	text = textract.process(fname)
	text = text.decode("utf-8") 
	f= open("texted_pdf.txt","w", encoding="utf-8")
	f.write(text)
	f.close()
	print("Text file successfully saved: texted_pdf.txt")
	# except:
	# input('Error found while converting pdf to a text file.')
	# sys.exit()
	return

full_directory = input('Enter the full directory of the PDF file: ')
extract_text_from_pdf(full_directory)
split_by_page = create_list_from_text_extracted_from_pdf()
print(split_by_page)

sys.exit()