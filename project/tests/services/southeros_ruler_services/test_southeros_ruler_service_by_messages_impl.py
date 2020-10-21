import unittest
from unittest.mock import patch

from main.models.kingdom import Kingdom
from main.models.ruler import Ruler
from main.services.kingdom_data_services.kingdom_data_service_csv_impl import KingdomDataServiceCsvImpl
from main.services.southeros_ruler_services.southeros_ruler_service_by_messages_impl import SoutherosRulerServiceByMessagesImpl


class SoutherosRulerServiceByMessagesImplTests(unittest.TestCase):
    def get_kingdoms(self):

        return {
            'TheMaroonKingdom': Kingdom('TheMaroonKingdom', 'Knight'),
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'JUNGLE': Kingdom('JUNGLE', 'Elephant'),
            'SEA': Kingdom('SEA', 'Shark')
        }

    @patch.object(KingdomDataServiceCsvImpl, 'get_all_kingdoms')
    def test_should_return_ruler(self, mocked_get_all_kingdoms):

        mocked_get_all_kingdoms.return_value = self.get_kingdoms()

        correct_ruler = Ruler(Kingdom('TheMaroonKingdom', 'Knight'), [
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

    def test_should_return_none(self):
        pass