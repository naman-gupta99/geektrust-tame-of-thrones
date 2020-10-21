import unittest

from main.models.kingdom import Kingdom
from main.utils.data_loader_factory import DataLoaderFactory


class DataLoaderFactoryTests(unittest.TestCase):

    __KINGDOM_CSV_FILE = 'kingdoms.csv'

    def test_should_return_correct_dictionary(self):
        """
        Should Load Correct Data and return
        """
        correct_data = [
            Kingdom('SPACE', 'Gorilla'),
            Kingdom('LAND', 'Panda'),
            Kingdom('WATER', 'Octopus'),
            Kingdom('ICE', 'Mammoth'),
            Kingdom('AIR', 'Owl'),
            Kingdom('FIRE', 'Dragon'),
        ]

        data_loader = DataLoaderFactory().get_data_loader('csv')

        result_data = data_loader(self.__KINGDOM_CSV_FILE)

        self.assertEqual(correct_data, result_data)