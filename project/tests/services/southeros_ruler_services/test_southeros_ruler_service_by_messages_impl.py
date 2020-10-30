import unittest
from unittest.mock import patch

from main.models.kingdom import Kingdom
from main.repository_services.kingdom_repository_services.kingdom_repository_service_csv_impl import KingdomRepositoryServiceCsvImpl
from main.services.southeros_ruler_services.southeros_ruler_service_by_messages_impl import SoutherosRulerServiceByMessagesImpl


class SoutherosRulerServiceByMessagesImplTests(unittest.TestCase):
    def get_kingdoms(self):
        """
        Helper Function to return Kingdoms Dictionary
        """

        return {
            'TheMaroonKingdom': Kingdom('TheMaroonKingdom', 'Knight'),
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'JUNGLE': Kingdom('JUNGLE', 'Elephant'),
            'SEA': Kingdom('SEA', 'Shark')
        }

    @patch.object(KingdomRepositoryServiceCsvImpl, 'get_all_kingdoms')
    def test_should_return_ruler(self, mocked_get_all_kingdoms):
        """
        Should return correct Ruler Object for correct messages
        """

        mocked_get_all_kingdoms.return_value = self.get_kingdoms()

        correct_ruler = Kingdom('TheMaroonKingdom', 'Knight', [
            Kingdom('SPACE', 'Gorilla'),
            Kingdom('JUNGLE', 'Elephant'),
            Kingdom('SEA', 'Shark')
        ])

        messages = {
            'SPACE': {'smzsNmpkvhmkzy'},
            'JUNGLE': {'popMinlavmxgbtb'},
            'SEA': {'pifxfXffxomkfw'}
        }

        result_ruler = SoutherosRulerServiceByMessagesImpl(
        ).check_ruler_of_southeros('TheMaroonKingdom', messages)

        self.assertEqual(correct_ruler, result_ruler)

    @patch.object(KingdomRepositoryServiceCsvImpl, 'get_all_kingdoms')
    def test_should_return_none(self, mocked_get_all_kingdoms):
        """
        Should return None for incorrect messages or less suppourt
        """

        mocked_get_all_kingdoms.return_value = self.get_kingdoms()

        correct_ruler = None

        messages = {
            'SPACE': {'smzsfsdafkssvhmkzy'},
            'JUNGLE': {'popvlzdddjkclxgbtb'},
            'SEA': {'pif'}
        }

        result_ruler = SoutherosRulerServiceByMessagesImpl(
        ).check_ruler_of_southeros('TheMaroonKingdom', messages)

        self.assertEqual(correct_ruler, result_ruler)