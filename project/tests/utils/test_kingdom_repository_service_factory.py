import unittest

from main.repository_services.kingdom_repository_services import *
from main.utils.kingdom_repository_service_factory import get_kingdom_repository_service


class KingdomRepositoryServiceFactoryTests(unittest.TestCase):
    def test_should_return_csv_impl(self):

        service = get_kingdom_repository_service('csv')()

        self.assertIsInstance(
            service,
            kingdom_repository_service_csv_impl.KingdomRepositoryServiceCsvImpl)
