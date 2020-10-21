from main.models.kingdom import Kingdom


class Ruler:
    """
    Model to represent Ruler of a universe
    """
    def __init__(self, ruler_kingdom: Kingdom, allies: list):
        """
        : ruler_kingdom : Kingdom Object of the Ruler Kingdom
        : allies : List of Kingdoms allies to the Ruler Kingdom
        """

        self.__ruler_kingdom = ruler_kingdom
        self.__allies = allies

    def __eq__(self, other):

        if not type(self) is type(other):
            return False
        
        if self.__ruler_kingdom != other.get_ruler_kingdom():
            return False
        
        for i, j in zip(self.__allies, other.get_allies()):
            if i != j:
                return False

        return True

    def __str__(self):

        return self.__ruler_kingdom.get_name() + " " + " ".join(
            [ally.get_name() for ally in self.__allies])

    """
    Getters and Setters
    """

    def get_ruler_kingdom(self):
        return self.__ruler_kingdom

    def get_allies(self):
        return self.__allies