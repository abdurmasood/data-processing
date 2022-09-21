from src.models.DataProcessingConfiguration import DataProcessingConfiguration
from src.models.NewColumn import NewColumn
from src.models.InputWorksheet import InputWorksheet
from src.models.OutputWorkbook import OutputWorkbook


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
                            output_workbook['remove_all_formatting'],
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
