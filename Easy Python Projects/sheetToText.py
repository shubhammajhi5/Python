import os


import openpyxl


def toTextFiles(filename):
    
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    count = 1

    for colObj in sheet.columns:
        
        with open('text-'+str(count)+'.txt', 'w') as file:
            for cellObj in colObj:
                file.write(cellObj.value)

        count += 1


if __name__ == "__main__":
    toTextFiles('worksheet.xlsx')