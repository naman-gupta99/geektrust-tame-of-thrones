import unittest
from unittest.mock import patch

from main.models.kingdom import Kingdom
from main.models.ruler import Ruler
from main.controllers.southeros_ruler_controller import SoutherosRulerController
from main.services.southeros_ruler_services.southeros_ruler_service_by_messages_impl import SoutherosRulerServiceByMessagesImpl


class SoutherosRulerControllerTests(unittest.TestCase):

    __CORRECT_MESSAGES_FILE_PATH = 'tests/resources/controllers/correct_messages.txt'
    __INCORRECT_MESSAGES_FILE_PATH = 'tests/resources/controllers/incorrect_messages.txt'
    __INCORRECT_FILE_PATH = 'tests/resources/controllers/incot_messages.txt'

    @patch.object(SoutherosRulerServiceByMessagesImpl, 'check_ruler_of_southeros')
    def test_should_return_ruler_kingdom_and_allies(self, mocked_check_ruler):

        mocked_check_ruler.return_value = Ruler(
            Kingdom('TheMaroonKingdom', 'Knight'), [
                Kingdom('SPACE', 'Gorilla'),
                Kingdom('JUNGLE', 'Elephant'),
                Kingdom('SEA', 'Shark')
            ])

        messages = {
            'SPACE': {'smzsNmpkvhmkzy'},
            'JUNGLE': {'popMinlavmxgbtb'},
            'SEA': {'pifxfXffxomkfw'}
        }

        correct_output = 'TheMaroonKingdom SPACE JUNGLE SEA'

        result_output = SoutherosRulerController(
        ).check_if_kingdom_is_ruler_using_input_file(
            'TheMaroonKingdom', self.__CORRECT_MESSAGES_FILE_PATH)

        mocked_check_ruler.assert_called_with('TheMaroonKingdom', messages)
        self.assertEqual(correct_output, result_output)

    @patch.object(SoutherosRulerServiceByMessagesImpl, 'check_ruler_of_southeros')
    def test_should_return_none(self, mocked_check_ruler):
        mocked_check_ruler.return_value = None

        messages = {
            'SPACE': {'smzsFDSmkzy'},
            'JUNGLE': {'popMiSDFASxgbtb'},
            'SEA': {'pifx'}
        }

        correct_output = 'NONE'

        result_output = SoutherosRulerController(
        ).check_if_kingdom_is_ruler_using_input_file(
            'TheMaroonKingdom', self.__INCORRECT_MESSAGES_FILE_PATH)

        mocked_check_ruler.assert_called_with('TheMaroonKingdom', messages)
        self.assertEqual(correct_output, result_output)

    def test_should_raise_file_not_found_error(self):
        
        with self.assertRaises(FileNotFoundError):
            SoutherosRulerController().check_if_kingdom_is_ruler_using_input_file('TheMaroonKnight', self.__INCORRECT_FILE_PATH)