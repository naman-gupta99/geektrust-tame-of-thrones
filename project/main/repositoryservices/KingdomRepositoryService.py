import abc

from main.models.Kingdom import Kingdom


class KingdomRepositoryService(metaclass=abc.ABCMeta):

    """
    Kingdom Repository Service Interface that can be used to build any future Repository Service
    """

    @abc.abstractmethod
    def get_all_kingdoms(self) -> dict:

        """
        Get Kingdoms from the Data Repository
        return Dictionsary(key: Kingdom Name, value: Ki9ngdom Object)
        """

        pass