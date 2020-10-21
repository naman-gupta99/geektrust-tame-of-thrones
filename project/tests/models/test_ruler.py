import unittest

from main.models.ruler import Ruler
from main.models.kingdom import Kingdom

class RulerTests(unittest.TestCase):

    def test_should_create_correct_object(self):
        """
        Should create correct object and return correct string
        """

        ruler_kingdom = Kingdom("TheMaroonKingdom", "Elephant")
        allies = [Kingdom("STAR", "Bull"), Kingdom("JUNGLE", "Tiger"), Kingdom("SWAMP", "Aligator")]

        correct_string = "TheMaroonKingdom STAR JUNGLE SWAMP"

        ruler = Ruler(ruler_kingdom, allies)

        result_string = str(ruler)

        self.assertEqual(correct_string, result_string)