import unittest

from main.services.kingdom_data_services import *
from main.utils.kingdom_data_service_factory import get_kingdom_data_service


class KingdomDataServiceFactoryTests(unittest.TestCase):
    def test_should_return_csv_impl(self):
        """
        Check if factory returns correct instance
        """
        service = get_kingdom_data_service('csv')()

        self.assertIsInstance(
            service, kingdom_data_service_csv_impl.KingdomDataServiceCsvImpl)
