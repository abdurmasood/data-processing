from os import listdir
from os.path import isfile, join
from src.globals import READ_DIR, CONFIG_FILE_PATH
import pandas as pd
import yaml


class DataReader:

    @staticmethod
    def read_yaml_configuration():
        """Reads a python dictionary based on YAML file.

        :returns:
            dict: Python dictionary based on the yaml config file.
        """
        with open(CONFIG_FILE_PATH, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def read_excel_workbook(workbook_name):
        """Reads a workbook from input folder.
        
        :param workbook_name: Name of workbook to read from the read directory.

        :returns:
            Pandas Excel Object: Pandas Excel file object with all worksheets.
        """
        return pd.ExcelFile(f'{READ_DIR}{workbook_name}')

    @staticmethod
    def read_excel_worksheet(workbook, worksheet_name):
        """Reads a worksheet from excel workbook.
        
        :param workbook: Pandas Workbook object to read from.
        :param worksheet_name: Name of worksheet to read from workbook.

        :returns:
            pd.Dataframe: Dataframe object containing worksheet data.
        """
        return workbook.parse(worksheet_name)

    @staticmethod
    def get_all_files_in_directory(directory):
        """Gets the names of all the files in a directory.

        :param directory: The directory from which to get the file names.
        
        :returns:
            list: A list with all the file names.
        """
        return [f for f in listdir(directory) if isfile(join(directory, f))]
