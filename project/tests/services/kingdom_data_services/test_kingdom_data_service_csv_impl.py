import unittest
from unittest.mock import patch

from main.models.kingdom import Kingdom
from main.repository_services.kingdom_repository_services.kingdom_repository_service_csv_impl import KingdomRepositoryServiceCsvImpl
from main.services.kingdom_data_services.kingdom_data_service_csv_impl import KingdomDataServiceCsvImpl


class KingdomDataServiceCsvImplTests(unittest.TestCase):
    @patch.object(KingdomRepositoryServiceCsvImpl, 'get_all_kingdoms')
    def test_should_return_correct_kingdom_data(
            self, mocked_get_all_kingdoms):

        """
        Should get data form repository and return
        """

        mocked_get_all_kingdoms.return_value = {
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'LAND': Kingdom('LAND', 'Panda'),
            'WATER': Kingdom('WATER', 'Octopus'),
            'ICE': Kingdom('ICE', 'Mammoth'),
            'AIR': Kingdom('AIR', 'Owl'),
            'FIRE': Kingdom('FIRE', 'Dragon')
        }

        correct_kingdoms = {
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'LAND': Kingdom('LAND', 'Panda'),
            'WATER': Kingdom('WATER', 'Octopus'),
            'ICE': Kingdom('ICE', 'Mammoth'),
            'AIR': Kingdom('AIR', 'Owl'),
            'FIRE': Kingdom('FIRE', 'Dragon')
        }

        result_kingdoms = KingdomDataServiceCsvImpl().get_all_kingdoms()

        for i in correct_kingdoms:

            self.assertEqual(correct_kingdoms[i], result_kingdoms[i])