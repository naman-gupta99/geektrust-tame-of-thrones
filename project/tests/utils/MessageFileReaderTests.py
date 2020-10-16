import unittest

from main.utils.MessageFileReader import read_messages_from_file

CORRECT_FORMAT_FILE_PATH = 'tests/resources/utils/MessageFileReader/correct_format_input.txt'


class MessageFileReaderTests(unittest.TestCase):
    def test_should_generate_message_dict(self):

        correct_messages = {
            'LAND': {'FAIJWJSOOFAMAU', 'dskajd'},
            'ICE': {'STHSTSTVSASOS'},
            'FIRE': {'JXGOOMUTOO'}
        }

        result_messages = read_messages_from_file(CORRECT_FORMAT_FILE_PATH)

        self.assertDictEqual(correct_messages, result_messages)
