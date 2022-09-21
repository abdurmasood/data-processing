class OutputWorkbook:

    def __init__(self, workbook_name=None, new_columns=None, remove_totals_row=None):
        self.workbook_name = workbook_name
        self.new_columns = new_columns
        self.remove_totals_row = remove_totals_row

    def __repr__(self):
        return f'OutputWorkbook({self.workbook_name}, ' \
               f'{self.new_columns}, ' \
               f'{self.remove_totals_row})'
