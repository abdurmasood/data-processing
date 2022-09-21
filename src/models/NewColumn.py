class NewColumn:

    def __init__(self, column_name=None, value_definition=None):
        self.column_name = column_name
        self.value_definition = value_definition

    def __repr__(self):
        return f'NewColumn({self.column_name}, {self.value_definition})'
