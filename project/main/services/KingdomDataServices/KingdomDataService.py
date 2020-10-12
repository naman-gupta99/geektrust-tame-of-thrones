import abc


class KingdomDataService(metaclass=abc.ABCMeta):
    """
    Service Interface to build any Services to get the Ruler of the Southeros
    """
    @abc.abstractmethod
    def get_all_kingdoms(self) -> list:
        """
        Use logic to find the Ruler of Southeros
        return Ruler Object
        """

        pass