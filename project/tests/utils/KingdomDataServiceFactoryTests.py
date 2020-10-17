import unittest

from main.services.KingdomDataServices import *
from main.utils.KingdomDataServiceFactory import get_kingdom_data_service


class KingdomDataServiceFactoryTests(unittest.TestCase):
    def test_should_return_csv_impl(self):

        service = get_kingdom_data_service('csv')()

        self.assertIsInstance(
            service, KingdomDataServiceCsvImpl.KingdomDataServiceCsvImpl)
