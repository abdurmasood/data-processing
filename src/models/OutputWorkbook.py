class OutputWorkbook:

    def __init__(self, workbook_name, new_columns, remove_all_formatting, remove_totals_row):
        self.workbook_name = workbook_name
        self.new_columns = new_columns
        self.remove_all_formatting = remove_all_formatting
        self.remove_totals_row = remove_totals_row
