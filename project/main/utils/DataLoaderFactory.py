
import csv
import os

from globals.configs import RESOURCES_DIR_PATH
from main.models.Kingdom import Kingdom

class DataLoaderFactory:

    """
    Factory class to generate Data Loaders
    """

    def get_data_loader(self, sourceType):
        if sourceType == 'csv':
            return _load_csv_data
        else:
            raise NotImplementedError("Data Loader with source type \"" + sourceType +"\" not implemented")

def _load_csv_data(kingdom_csv: str):

    """
    Loads Data given in the input csv file present in the resources folder
    The Format:
        Kingdom Name, Kingdom Emblem
    """

    file_path = os.getcwd() + '\\' + RESOURCES_DIR_PATH + '\\' + kingdom_csv
    
    kingdomArr = []

    with open(file_path, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            kingdomArr.append(Kingdom(row[0], row[1]))

    print([(i.name, i.emblem) for i in kingdomArr])