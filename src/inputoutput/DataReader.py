from os import listdir
from os.path import isfile, join
import pandas as pd
import yaml


class DataReader:

    def __init__(self):
        self.config_path = './../config.yaml'
        self.read_path = './../data/input/'

    def read_yaml_configuration(self):
        """
        Reads a python dictionary based on YAML file.
        :param file_path: The path to the YAML file to read.
        :return: Python dictionary based on the yaml config file
        """
        with open(self.config_path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def read_excel_workbook(self, workbook_name):
        """
        Reads a workbook from input folder.
        :param workbook_name: The name of the worksheet to read.
        :return: Pandas Excel file object with all worksheets
        """
        return pd.ExcelFile(f'{self.read_path}{workbook_name}')

    @staticmethod
    def read_excel_worksheet(workbook, worksheet_name):
        """
        Reads a worksheet from an Excel workbook.
        :param workbook: Workbook Object read by pandas.
        :param worksheet_name: 
        :return: Dataframe with worksheet details.
        """
        return workbook.parse(worksheet_name)

    @staticmethod
    def get_all_files_in_directory(directory):
        """
        Gets the names of all the files in a directory.
        :param directory: The directory from which to get the file names.
        :return: A list with all the file names.
        """
        return [f for f in listdir(directory) if isfile(join(directory, f))]
