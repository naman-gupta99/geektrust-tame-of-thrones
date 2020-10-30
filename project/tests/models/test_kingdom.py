import unittest
from unittest.mock import patch

from main.models.kingdom import Kingdom
from main.utils.ciphers.seasar_cipher_util import SeasarCipherUtil

class KingdomTests(unittest.TestCase):

    def test_should_create_correct_object(self):
        """
        Should convert to string correctly
        """

        correct_string = 'TheMaroonKingdom '

        kingdom = Kingdom('TheMaroonKingdom', 'Elephant')

        result_string = str(kingdom)

        self.assertEqual(correct_string, result_string)

    @patch.object(SeasarCipherUtil, 'decrypt')
    def test_should_ally_on_recieving_correct_message(self, mocked_decrypt):
        """
        Should return Ally response for the correct response
        """

        mocked_decrypt.return_value = 'elfase phfadsd afadsss dnd ast'

        correct_response = True

        kingdom = Kingdom('TheMaroonKingdom', 'Elephant')
        result_response = kingdom.recieve_message('mtniam xpnilal inilaaa lvl iab')

        mocked_decrypt.assert_called_with('mtniam xpnilal inilaaa lvl iab', 8)
        self.assertEqual(correct_response, result_response)

    @patch.object(SeasarCipherUtil, 'decrypt')
    def test_should_recieve_support_from_other_kingdom(self, mocked_decrypt):
        """
        Should recieve ally message when sends correct message
        """

        mocked_decrypt.return_value = 'elfase phfadsd afadsss dnd ast'

        correct_response = True

        reciever_kingdom = Kingdom('TheMaroonKingdom', 'Elephant')
        sender_kingdom = Kingdom('SPACE', 'Gorilla')
        result_response = sender_kingdom.send_message(reciever_kingdom, 'mtniam xpnilal inilaaa lvl iab')

        mocked_decrypt.assert_called_with('mtniam xpnilal inilaaa lvl iab', 8)
        self.assertEqual(correct_response, result_response)

    def test_should_evaluate_right_allies(self):

        kingdoms = {
            'TheMaroonKingdom': Kingdom('TheMaroonKingdom', 'Knight'),
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'JUNGLE': Kingdom('JUNGLE', 'Elephant'),
            'SEA': Kingdom('SEA', 'Shark')
        }

        messages = {
            'SPACE': {'smzsNmpkvhmkzy'},
            'JUNGLE': {'popMinlavmxgbtb'},
            'SEA': {'pif'}
        }

        correct_allies = [kingdoms['SPACE'], kingdoms['JUNGLE']]

        kingdom = Kingdom('TheMaroonKingdom', 'Knight')

        kingdom.evaluate_allies(kingdoms, messages)

        result_allies = kingdom.get_allies()

        self.assertEqual(correct_allies, result_allies)