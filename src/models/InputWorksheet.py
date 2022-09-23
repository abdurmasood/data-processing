class InputWorksheet:

    def __init__(self, sheet_name, output_workbooks, remove_totals_row=None):
        self.sheet_name = sheet_name
        self.output_workbooks = output_workbooks
        self.remove_totals_row = remove_totals_row

    def __repr__(self):
        return f'InputWorksheet({self.sheet_name}, {self.output_workbooks}, {self.remove_totals_row})'
