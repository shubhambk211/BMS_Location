import xlrd
from Library.config import Config


def read_locators():
    workbook = xlrd.open_workbook(Config.DATA_PATH)
    worksheet = workbook.sheet_by_name('location')
    rows = worksheet.nrows
    print(rows)
    d = {}

    for i in range(1,rows):
        row = worksheet.row_values(i)
        d[row[0]] =(row[1],row[2])
    return d


print(read_locators())


def read_data():
    workbook = xlrd.open_workbook(Config.DATA_PATH)
    worksheet = workbook.sheet_by_name('data')
    rows = worksheet.get_rows()
    columns = worksheet.ncols
    header = next(rows)
    data = []
    for row in rows:
        values = ()
        for j in range(columns):
            values += (row[j].value,)
        data.append(values)
    return data


print(read_data())