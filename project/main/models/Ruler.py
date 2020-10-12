from main.models.Kingdom import Kingdom


class Ruler:

    """
    Model to represent Ruler of a universe
    """

    def __init__(self, ruler_kingdom: Kingdom, allies: list):

        """
        : ruler_kingdom : Kingdom Object of the Ruler Kingdom
        : allies : List of Kingdoms allies to the Ruler Kingdom
        """

        self.ruler_kingdom = ruler_kingdom
        self.allies = allies

    def __str__(self):

        return self.ruler_kingdom.name + " " + " ".join([ally.name for ally in allies])
