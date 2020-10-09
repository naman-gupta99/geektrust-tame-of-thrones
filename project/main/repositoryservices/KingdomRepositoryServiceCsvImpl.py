from globals.configs import KINGDOM_CSV_PATH
from main.repositoryservices.KingdomRepositoryService import KingdomRepositoryService
from main.utils.DataLoaderFactory import DataLoaderFactory


class KingdomRepositoryServiceCsvImpl(KingdomRepositoryService):
    def __init__(self):

        """
        Initialize Object by loading Kingdom Data from CSV file
        """

        data_loader = DataLoaderFactory().get_data_loader("csv")
        kingdom_arr = data_loader(KINGDOM_CSV_PATH)

        self.kingdom_data = dict((kingdom.name, kingdom) for kingdom in kingdom_arr)

    def get_all_kingdoms(self):

        return self.kingdom_data
