from src.models.DataProcessingConfiguration import DataProcessingConfiguration
from src.models.NewColumn import NewColumn
from src.models.InputWorksheet import InputWorksheet
from src.models.OutputWorkbook import OutputWorkbook
import string


class DataFormattingService:
    def __init__(self):
        pass

    @staticmethod
    def remove_totals_line(dataframe):
        for col in dataframe:
            element = str(dataframe[col][dataframe.index[-1]])
            if element:
                if element.lower() == 'total':
                    dataframe.drop(dataframe.tail(1).index, inplace=True)

    @staticmethod
    def parse_yaml(yaml):
        input_worksheets = []

        # Parsing the yaml file into the relevant models.
        for input_worksheet in yaml['sheets']:
            output_workbooks = []

            # check for output_workbook configuration in yaml and create ORM for OutputWorkbook
            if 'output_workbooks' in input_worksheet:
                for output_workbook in input_worksheet['output_workbooks']:
                    new_columns = []

                    # check for new columns configuration in yaml and create ORM for NewColumn
                    if 'new_columns' in output_workbook:
                        for new_column in output_workbook['new_columns']:
                            new_columns.append(
                                NewColumn(
                                    new_column['column_name'],
                                    new_column['value_definition']
                                )
                            )

                    output_workbooks.append(
                        OutputWorkbook(
                            output_workbook['workbook_name'],
                            new_columns,
                            output_workbook['remove_totals_row']
                        )
                    )

            input_worksheets.append(
                InputWorksheet(
                    input_worksheet['sheet_name'],
                    output_workbooks
                )
            )

        return DataProcessingConfiguration(
            input_worksheets
        )

    @staticmethod
    def index_to_excel_column(column_index):
        start_index = 1  # it can start either at 0 or at 1
        letter = ''
        while column_index > 25 + start_index:
            letter += chr(65 + int((column_index - start_index) / 26) - 1)
            column_index = column_index - (int((column_index - start_index) / 26)) * 26
        letter += chr(65 - start_index + (int(column_index)))

        return letter

    @staticmethod
    def excel_column_to_index(excel_column_string):
        num = 0
        for c in excel_column_string:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1

        return num
