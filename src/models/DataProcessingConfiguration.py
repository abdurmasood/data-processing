class DataProcessingConfiguration:

    def __init__(self, input_worksheets):
        self.input_worksheets = input_worksheets

    def __repr__(self):
        return f'DataProcessingConfiguration({self.input_worksheets})'
