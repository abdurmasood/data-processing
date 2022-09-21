class DataProcessingConfiguration:

    def __init__(self, input_worksheets=None, remove_totals_row=None):
        self.input_worksheets = input_worksheets
        self.remove_totals_row = remove_totals_row

    def __repr__(self):
        return f'DataProcessingConfiguration({self.input_worksheets}, {self.remove_totals_row})'
