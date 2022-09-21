class InputWorksheet:

    def __init__(self, sheet_name, output_workbooks):
        self.sheet_name = sheet_name
        self.output_workbooks = output_workbooks

    def __repr__(self):
        return f'InputWorksheet({self.sheet_name}, {self.output_workbooks})'
