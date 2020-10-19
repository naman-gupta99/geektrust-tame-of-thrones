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

    def __str__(self):

        return self.__ruler_kingdom.get_name() + " " + " ".join(
            [ally.get_name() for ally in self.__allies])
