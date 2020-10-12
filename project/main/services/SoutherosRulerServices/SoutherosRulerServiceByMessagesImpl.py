from globals.configs import DATA_LOADING_SOURCE
from main.models.Kingdom import Kingdom
from main.models.Ruler import Ruler
from main.services.SoutherosRulerServices.SoutherosRulerService import (
    SoutherosRulerService,
)
from main.utils.KingdomRepositoryServiceFactory import get_kingdom_repository_service


class SoutherosRulerServiceByMessagesImpl(SoutherosRulerService):
    """
    Service to get if a Kingdom can become Ruler of Southeros by Sending Messages to all the other
    Kingdoms and finding out how many and which kingdoms are allies of the current Kingdom
    """

    def __init__(self):
        """
        Initialize object by getting the Repository Service Object
        """

        kingdom_repository_service_class = get_kingdom_repository_service(
            DATA_LOADING_SOURCE
        )
        self.kingdom_repository_service = kingdom_repository_service_class()

    def check_ruler_of_southeros(self, curr_kingdom: str, messages: dict) -> Ruler:
        """
        Send messages to all the kingdoms and check the allies
        Return Ruler for the current kingdom if it is the Ruler else send None
        """

        return None