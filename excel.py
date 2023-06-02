import openpyxl
import os

os.getcwd()

def search_long_lat(SelectedTestCase, input ,type):
    ps = openpyxl.load_workbook('data_order.xlsx')
    sheet = ps[SelectedTestCase]
    koordinat = ''
    
    for row in sheet.iter_rows(min_row=1, min_col=2, max_row=11, max_col=11, values_only=False):
        for cell in row:
            if cell.value == input:
                
                if type == "tujuan":
                    tujuan_lat = sheet['M' + str(cell.row)].value
                    tujuan_lang = sheet['N' + str(cell.row)].value
                    koordinat = str(tujuan_lat)+ ',' + str(tujuan_lang)
                   
                elif type == "asal":
                    asal_lat = sheet['G' + str(cell.row)].value
                    asal_lang = sheet['H' + str(cell.row)].value
                    koordinat = str(asal_lat)+ ',' + str(asal_lang)
                    break
                        
        
    return koordinat