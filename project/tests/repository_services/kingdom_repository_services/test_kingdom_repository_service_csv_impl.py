import csv
import os
import unittest
from unittest.mock import patch

from main.models.kingdom import Kingdom
from main.repository_services.kingdom_repository_services.kingdom_repository_service_csv_impl import KingdomRepositoryServiceCsvImpl
from main.utils.data_loader_factory import DataLoaderFactory

KINGDOM_CSV_PATH = 'tests/resources/repository_services/kingdom_repository_service/kingdoms.csv'


def mock_data_loader(csv_path):
    """
    Mock Data loader that loads Data from our testing Repository
    """
    file_path = KINGDOM_CSV_PATH

    kingdomArr = []

    with open(file_path, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            kingdomArr.append(Kingdom(row[0], row[1]))

    return kingdomArr


class KingdomRepositoryServicesCsvImplTests(unittest.TestCase):
    @patch.object(DataLoaderFactory, 'get_data_loader')
    def test_should_return_correct_data(self, mocked_get_data_loader):
        """
        Check if the repository returns correct data
        """

        mocked_get_data_loader.return_value = mock_data_loader

        correct_kingdoms = {
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'LAND': Kingdom('LAND', 'Panda'),
            'WATER': Kingdom('WATER', 'Octopus'),
            'ICE': Kingdom('ICE', 'Mammoth'),
            'AIR': Kingdom('AIR', 'Owl'),
            'FIRE': Kingdom('FIRE', 'Dragon')
        }

        result_kingdoms = KingdomRepositoryServiceCsvImpl().get_all_kingdoms()

        for i in correct_kingdoms:

            self.assertEqual(correct_kingdoms[i], result_kingdoms[i])