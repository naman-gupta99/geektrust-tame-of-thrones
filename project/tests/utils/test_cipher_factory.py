import unittest

from main.utils.cipher_factory import get_cipher_util
from main.utils.ciphers import *


class CipherFactoryTests(unittest.TestCase):

    __CIPHER_TECHNIQUE = 'Seasar'

    def setUp(self):
        self.result_cipher = get_cipher_util(self.__CIPHER_TECHNIQUE)()

    def test_should_return_seasar_cipher(self):

        self.assertIsInstance(self.result_cipher,
                              seasar_cipher_util.SeasarCipherUtil)

    def test_cipher_should_encrypt_plain_text(self):

        plain_text_and_key_arr = [('HELLO', 3), ('Random Tales', 7),
                                  ('tHeMaAroOnKnIgHt', 2), ('Cosmos', 1),
                                  ('abcdefgh', 4)]
        correct_cipher_text_arr = [
            'KHOOR', 'Yhukvt Ahslz', 'vJgOcCtqQpMpKiJv', 'Dptnpt', 'efghijkl'
        ]

        result_cipher_text_arr = []

        for plain_text, key in plain_text_and_key_arr:
            result_cipher_text_arr.append(
                self.result_cipher.encrypt(plain_text, key))

        self.assertEqual(correct_cipher_text_arr, result_cipher_text_arr)

    def test_cipher_should_decrypt_cipher_text(self):

        cipher_text_and_key_arr = [('KHOOR', 3), ('Yhukvt Ahslz', 7),
                                  ('vJgOcCtqQpMpKiJv', 2), ('Dptnpt', 1),
                                  ('efghijkl', 4)]
        correct_plain_text_arr = [
            'HELLO', 'Random Tales', 'tHeMaAroOnKnIgHt', 'Cosmos', 'abcdefgh'
        ]

        result_plain_text_arr = []

        for cipher_text, key in cipher_text_and_key_arr:
            result_plain_text_arr.append(
                self.result_cipher.decrypt(cipher_text, key))

        self.assertEqual(correct_plain_text_arr, result_plain_text_arr)