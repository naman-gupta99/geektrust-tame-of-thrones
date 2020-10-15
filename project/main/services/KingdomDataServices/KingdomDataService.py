import abc


class KingdomDataService(metaclass=abc.ABCMeta):
    """
    Kingdom Data Service to build a Service to get Data from Repository Service
    """

    @abc.abstractmethod
    def get_all_kingdoms(self) -> list:
        """
        Get all the Kingdoms from Repository Service
        return list of Kingdoms
        """

        pass