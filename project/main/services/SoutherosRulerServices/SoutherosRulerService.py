import abc

from main.models.Ruler import Ruler


class SoutherosRulerService(metaclass=abc.ABCMeta):
    """
    Service Interface to build any Services to get the Ruler of the Southeros
    """
    @abc.abstractmethod
    def check_ruler_of_southeros(self, current_kingdom_name: str,
                                 messages: dict) -> Ruler:
        """
        Use logic to find the Ruler of Southeros
        return Ruler Object
        """

        pass