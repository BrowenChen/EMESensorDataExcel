__author__ = 'owenchen'

#EME Systems LLC
#-----
#
#Takes data from sensor and calculates statistical variance with xldr libra
#Documentation for xldr functions:
#http://www.lexicon.net/sjmachin/xlrd.html
#http://www.simplistix.co.uk/presentations/python-excel.pdf

import xlrd

file_loc = "data.xls"
wb = xlrd.open_workbook(file_loc)

#Some variables
sheet = wb.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols

print(" ")
print("Iterate_Freq function can either output the low, mid, or high frequencies. Parameter is 1 for low, "
      "2 for mid, and 3 for high")


#Iterates through the first column of the excel data file, which include seconds
def iterate_seconds():
    for row in range(sheet.nrows):
        print(sheet.cell_value(row, 0))

#This iterates through the frequencies
def iterate_Freq(choice):
    if choice == 1:
            print("Printing low frequencies")
    elif choice == 2:
            print("Printing mid frequencies")
    elif choice == 3:
            print("Printing high frequencies")

    for row in range(sheet.nrows):
        print(sheet.cell_value(row, choice))



def calculate_variance():
    



