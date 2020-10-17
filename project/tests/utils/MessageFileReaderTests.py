import unittest

from main.utils.MessageFileReader import read_messages_from_file


class MessageFileReaderTests(unittest.TestCase):

    __CORRECT_FORMAT_FILE_PATH = 'tests/resources/utils/MessageFileReader/correct_format_input.txt'
    __INCORRECT_FORMAT_FILE_PATH = 'tests/resources/utils/MessageFileReader/INcorrect_format_input.txt'

    def test_should_generate_message_dict(self):

        correct_messages = {
            'LAND': {'FAIJWJSOOFAMAU', 'dskajd'},
            'ICE': {'STHSTSTVSASOS'},
            'FIRE': {'JXGOOMUTOO'}
        }

        result_messages = read_messages_from_file(
            self.__CORRECT_FORMAT_FILE_PATH)

        self.assertDictEqual(correct_messages, result_messages)

    def test_should_raise_io_erorr(self):

        with self.assertRaises(IOError):
            read_messages_from_file(self.__INCORRECT_FORMAT_FILE_PATH)
