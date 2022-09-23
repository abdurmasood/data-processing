from src.services.DataFormattingService import DataFormattingService as formatter
from src.inputoutput.DataReader import DataReader as datareader
from src.inputoutput.DataWriter import DataWriter as datawriter


class RuleService:
    def __init__(self, workbook_name=None):
        self.workbook_name = workbook_name
        self.operators_to_process = ['+', '-', '*', '/']

    def parse_configuration_rules(self):
        """
        Read and parse yaml configuration. Use the configuration to create new workbooks based on specified workbook.
        """

        # Parsing the workbook name to get the month and year.
        month, year = formatter.parse_workbook_name(self.workbook_name)

        # Reading the yaml file and parsing it into a dictionary.
        data_processing_cofiguration = formatter.parse_yaml(
            datareader.read_yaml_configuration()
        )

        workbook = datareader.read_excel_workbook(self.workbook_name)

        for input_worksheet in data_processing_cofiguration.input_worksheets:
            sheet_df = datareader.read_excel_worksheet(workbook, input_worksheet.sheet_name)

            if input_worksheet.remove_totals_row:
                formatter.remove_totals_row(sheet_df)

            if input_worksheet.output_workbooks:

                for output_workbook in input_worksheet.output_workbooks:

                    if output_workbook.remove_totals_row:
                        formatter.remove_totals_row(sheet_df)

                    if output_workbook.new_columns:

                        for new_column in output_workbook.new_columns:
                            sheet_df = self.calculate_new_column(
                                new_column.column_name,
                                new_column.value_definition,
                                sheet_df
                            )

                    datawriter.create_excel_workbook(
                        year=year,
                        month=month,
                        sheet_name=input_worksheet.sheet_name.upper(),
                        workbook_name=output_workbook.workbook_name,
                        data=sheet_df
                    )
            else:

                datawriter.create_excel_workbook(
                    year=year,
                    month=month,
                    sheet_name=input_worksheet.sheet_name.upper(),
                    data=sheet_df
                )

    def calculate_new_column(self, column_name, value_definition, df):
        """
        Create new column in dataframe and populate it with values based on a mathematical formula passed into the
        function.

        :param column_name: Name of new column to create.
        :param value_definition: Mathematical formula passed as string.
        :param df: Pandas dataframe to manipulate.
        :return:
            pd.Dataframe: Dataframe with newly populated column.
        """
        for operator in self.operators_to_process:
            if operator in value_definition:
                sub_formulas = value_definition.split(operator)
                column1_index = formatter.excel_column_to_index(sub_formulas[0])
                column2_index = formatter.excel_column_to_index(sub_formulas[1])

                column1 = df.iloc[:, column1_index]
                column2 = df.iloc[:, column2_index]

                df[column_name] = formatter.dataframe_column_processing(column1, column2, operator)
                break
            else:
                pass

        return df
