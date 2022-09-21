from src.inputoutput.DataReader import DataReader
from src.services.DataFormattingService import DataFormattingService


class RuleService:
    def __init__(self, workbook_name_to_read=None):
        self.workbook_name_to_read = workbook_name_to_read
        self.data_reader = DataReader()

    def parse_configuration_rules(self):
        # Reading the yaml file and parsing it into a dictionary.
        data_processing_cofiguration = DataFormattingService.parse_yaml(
            self.data_reader.read_yaml_configuration()
        )

        for input_worksheet in data_processing_cofiguration.input_worksheets:
            if input_worksheet.output_workbooks:
                for output_workbook in input_worksheet.output_workbooks:
                    # create output_workbooks in write directory
                    # parse data as a dataframe
                    # format data in data frame and remove totals row

                    if output_workbook.new_columns:
                        for new_column in output_workbook.new_columns:
                            # add new columns dataframe
                            # do calculation of values based on value definition defined for new column in yaml
                            pass

                    # write dataframe to output workbook
