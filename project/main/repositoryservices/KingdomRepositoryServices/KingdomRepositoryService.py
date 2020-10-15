import abc

from main.models.Kingdom import Kingdom


class KingdomRepositoryService(metaclass=abc.ABCMeta):

    """
    Kingdom Repository Service Interface ton be used to build any Repository Services
    """

    @abc.abstractmethod
    def get_all_kingdoms(self) -> dict:

        """
        Get Kingdoms from the Data Repository
        return Dictionary(key: Kingdom Name, value: Ki9ngdom Object)
        """

        pass