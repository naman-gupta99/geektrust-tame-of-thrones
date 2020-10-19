from globals.configs import DATA_LOADING_SOURCE, KINGDOM_CSV_PATH
from main.repositoryservices.kingdom_repository_services.kingdom_repository_service import (
    KingdomRepositoryService, )
from main.utils.data_loader_factory import DataLoaderFactory


class KingdomRepositoryServiceCsvImpl(KingdomRepositoryService):
    """
    Kingdom Repository Service to get Kindom Data from CSV file
    """
    def __init__(self):
        """
        Initialize Object by loading repository information
        """

        self.__data_loader = DataLoaderFactory().get_data_loader(
            DATA_LOADING_SOURCE)

    def get_all_kingdoms(self):
        """
        Return Dictionary of Kingdoms loaded from csv file
        """

        kingdom_arr = self.__data_loader(KINGDOM_CSV_PATH)
        kingdom_data = dict(
            (kingdom.get_name(), kingdom) for kingdom in kingdom_arr)

        return kingdom_data
