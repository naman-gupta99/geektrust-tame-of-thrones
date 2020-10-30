from globals.configs import DATA_LOADING_SOURCE
from main.models.kingdom import Kingdom
from main.services.southeros_ruler_services.southeros_ruler_service import (
    SoutherosRulerService, )
from main.utils.kingdom_repository_service_factory import get_kingdom_repository_service


class SoutherosRulerServiceByMessagesImpl(SoutherosRulerService):
    """
    Service to get if a Kingdom can become Ruler of Southeros by Sending Messages to all the other
    Kingdoms and finding out how many and which kingdoms are allies of the current Kingdom
    """
    def __init__(self):
        """
        Initialize object by getting the Repository Service Object
        """

        self.__kingdom_repository_service = get_kingdom_repository_service(
            DATA_LOADING_SOURCE)()

    def check_ruler_of_southeros(self, curr_kingdom_name: str,
                                 messages: dict) -> Kingdom:
        """
        Send messages to all the kingdoms and check the allies
        Return Kingdom for the current kingdom if it is the Ruler else send None
        """

        kingdoms = self.__kingdom_repository_service.get_all_kingdoms()

        curr_kingdom = kingdoms[curr_kingdom_name]

        curr_kingdom.evaluate_allies(kingdoms, messages)

        if len(curr_kingdom.get_allies()) >= 3:
            return curr_kingdom
        else:
            return None