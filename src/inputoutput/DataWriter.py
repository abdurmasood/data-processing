import openpyxl
import pandas as pd

from src.globals import WRITE_DIR


class DataWriter:
    @staticmethod
    def create_excel_workbook(year, month, sheet_name, workbook_name='', data=None):
        """
        Creates a new Excel workbook in the write directory. User can specify if any data needs to be stored in excel
        file.

        :param year: Year when data was collected.
        :param month: Month when data was collected.
        :param sheet_name: Name of sheet that data is being taken from.
        :param workbook_name: Name of workbook that data is being taken from.
        :param data: Data to write to newly created Excel file.
        """
        writer = pd.ExcelWriter(f'{WRITE_DIR}{year}{month} {sheet_name} {workbook_name}.xlsx')
        data.to_excel(writer)
        writer.save()
        writer.close()
