import openpyxl

from src.globals import WRITE_DIR


class DataWriter:
    @staticmethod
    def create_excel_workbook(year, month, sheet_name, workbook_name):
        """
        Creates a new Excel workbook in the write directory.
        :param workbook_name:
        :param sheet_name:
        :param year:
        :param month:
        """
        wb = openpyxl.Workbook()
        wb.save(f'{WRITE_DIR}{year}{month} {sheet_name} {workbook_name}.xlsx')
        wb.close()

