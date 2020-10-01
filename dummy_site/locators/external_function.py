import openpyexcel
from dummy_site.test_data.data_dummy import excel_file_path

def get_cell_data(rows, colns, filepath=excel_file_path):
    workbook = openpyexcel.load_workbook(filepath)
    sheet = workbook.active
    print(sheet)
    data = sheet.cell(rows, colns)
    return data.value