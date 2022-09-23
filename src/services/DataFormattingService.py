from src.models.DataProcessingConfiguration import DataProcessingConfiguration
from src.models.NewColumn import NewColumn
from src.models.InputWorksheet import InputWorksheet
from src.models.OutputWorkbook import OutputWorkbook
import string


class DataFormattingService:
    def __init__(self):
        pass

    @staticmethod
    def remove_totals_row(dataframe):
        """
        Function to remove Totals row from dataframe (if present)

        :param dataframe: Pandas dataframe to manipulate
        """
        for col in dataframe:
            element = str(dataframe[col][dataframe.index[-1]])
            if element:
                if element.lower() == 'total':
                    dataframe.drop(dataframe.tail(1).index, inplace=True)

    @staticmethod
    def parse_yaml(yaml):
        """
        Parse yaml configuration and store values in python defined models in src.models.

        :param yaml: Yaml to parse.
        :return:
            DataProcessingConfiguration: Python model that stores all yaml configuration.
        """
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

            if 'remove_totals_row' in input_worksheet:
                input_worksheets.append(
                    InputWorksheet(
                        input_worksheet['sheet_name'],
                        output_workbooks,
                        input_worksheet['remove_totals_row']
                    )
                )
            else:
                input_worksheets.append(
                    InputWorksheet(
                        input_worksheet['sheet_name'],
                        output_workbooks
                    )
                )

        if 'remove_totals_row' in yaml:
            return DataProcessingConfiguration(
                input_worksheets,
                yaml['remove_totals_row']
            )
        else:
            return DataProcessingConfiguration(
                input_worksheets
            )

    @staticmethod
    def parse_workbook_name(name):
        """
        Parse workbook name to get the month and year of data collection.

        :param name: Name of workbook to parse.
        :return:
            month: Month of data collection
            year: Year of data collection
        """
        name_split = name.split('_')
        month_year = name_split[2]
        file_name = name_split[3]

        month = month_year.split('.')[0]
        year = month_year.split('.')[1]
        return month, year

    @staticmethod
    def index_to_excel_column(column_index):
        """
        Function to convert integer based index to an Excel column index.

        :param column_index: Index to convert to excel column index.
        :return:
            letter: Equivalent excel based column index
        """
        start_index = 1
        letter = ''
        while column_index > 25 + start_index:
            letter += chr(65 + int((column_index - start_index) / 26) - 1)
            column_index = column_index - (int((column_index - start_index) / 26)) * 26
        letter += chr(65 - start_index + (int(column_index)))

        return letter

    @staticmethod
    def excel_column_to_index(excel_column_string):
        """
        Function to convert excel column to integer based index.

        :param excel_column_string: Excel column index to convert.
        :return:
            num: Integer based index
        """
        num = 0
        for c in excel_column_string:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1

        return num - 1

    @staticmethod
    def dataframe_column_processing(column1, column2, processing_operator):
        """
        Function to perform mathematical functions on two dataframe columns.

        :param column1: Column 1 from dataframe.
        :param column2: Column 2 from dataframe.
        :param processing_operator: Mathematical operation to perform.
        :return:
            result: Dataframe after the mathematical function has been applied
        """
        result = None

        if processing_operator == '/':
            result = column1/column2
        elif processing_operator == '*':
            result = column1*column2
        elif processing_operator == '+':
            result = column1+column2
        elif processing_operator == '-':
            result = column1-column2

        return result
