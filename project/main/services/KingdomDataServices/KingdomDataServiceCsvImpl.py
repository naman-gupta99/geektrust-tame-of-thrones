from globals.configs import DATA_LOADING_SOURCE
from main.services.KingdomDataServices.KingdomDataService import KingdomDataService
from main.utils.KingdomRepositoryServiceFactory import get_kingdom_repository_service


class KingdomDataServiceCsvImpl(KingdomDataService):
    """
    Service to get data pesent in the Kingdom Repository
    """
    def __init__(self):
        """
        Initialize object by getting the Repository Service Object
        """

        kingdom_repository_service_class = get_kingdom_repository_service(
            DATA_LOADING_SOURCE)
        self.kingdom_repository_service = kingdom_repository_service_class()

    def get_all_kingdoms(self) -> dict:

        return self.kingdom_repository_service.get_all_kingdoms()
