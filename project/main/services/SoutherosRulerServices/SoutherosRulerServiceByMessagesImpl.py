from globals.configs import DATA_LOADING_SOURCE
from main.models.Kingdom import Kingdom
from main.models.Ruler import Ruler
from main.services.SoutherosRulerServices.SoutherosRulerService import (
    SoutherosRulerService,
)
from main.utils.KingdomDataServiceFactory import get_kingdom_data_service


class SoutherosRulerServiceByMessagesImpl(SoutherosRulerService):
    """
    Service to get if a Kingdom can become Ruler of Southeros by Sending Messages to all the other
    Kingdoms and finding out how many and which kingdoms are allies of the current Kingdom
    """

    def __init__(self):
        """
        Initialize object by getting the Repository Service Object
        """

        self.kingdom_data_service = get_kingdom_data_service(DATA_LOADING_SOURCE)()

    def check_ruler_of_southeros(self, curr_kingdom_name: str, messages: dict) -> Ruler:
        """
        Send messages to all the kingdoms and check the allies
        Return Ruler for the current kingdom if it is the Ruler else send None
        """

        kingdoms = self.kingdom_data_service.get_all_kingdoms()

        curr_kingdom = kingdoms[curr_kingdom_name]

        allies = []

        for kingdom_name in messages:
            if kingdom_name != curr_kingdom_name:
                for message in messages[kingdom_name]:
                    if curr_kingdom.send_message(kingdoms[kingdom_name], message):
                        allies.append(kingdoms[kingdom_name])
                        break

        if len(allies) >= 3:
            return Ruler(curr_kingdom, allies)
        else:
            return None