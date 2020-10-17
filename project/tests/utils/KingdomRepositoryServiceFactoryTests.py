import unittest

from main.repositoryservices.KingdomRepositoryServices import *
from main.utils.KingdomRepositoryServiceFactory import get_kingdom_repository_service


class KingdomRepositoryServiceFactoryTests(unittest.TestCase):
    def test_should_return_csv_impl(self):

        service = get_kingdom_repository_service('csv')()

        self.assertIsInstance(
            service,
            KingdomRepositoryServiceCsvImpl.KingdomRepositoryServiceCsvImpl)
