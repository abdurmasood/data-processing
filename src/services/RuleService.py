from src.services.DataFormattingService import DataFormattingService as formatter
from src.inputoutput.DataReader import DataReader as datareader
from src.inputoutput.DataWriter import DataWriter as datawriter


class RuleService:
    def __init__(self, workbook_name=None):
        self.workbook_name = workbook_name
        self.operators_to_process = ['+', '-', '*', '/']

    def parse_configuration_rules(self):
        # Parsing the workbook name to get the month and year.
        month, year = formatter.parse_workbook_name(self.workbook_name)

        # Reading the yaml file and parsing it into a dictionary.
        data_processing_cofiguration = formatter.parse_yaml(
            datareader.read_yaml_configuration()
        )

        # read workbook
        workbook = datareader.read_excel_workbook(self.workbook_name)

        for input_worksheet in data_processing_cofiguration.input_worksheets:
            if input_worksheet.output_workbooks:
                # Reading the worksheet from the workbook as dataframe.
                sheet_df = datareader.read_excel_worksheet(workbook, input_worksheet.sheet_name)

                for output_workbook in input_worksheet.output_workbooks:
                    # Creating a new excel workbook in the output directory.
                    datawriter.create_excel_workbook(
                        year,
                        month,
                        input_worksheet.sheet_name.upper(),
                        output_workbook.workbook_name
                    )

                    if output_workbook.new_columns:
                        for new_column in output_workbook.new_columns:
                            # create new columns in sheet_df based on yaml configuration
                            # fill column values based on value definition
                            pass

                    # write dataframe to output workbook
