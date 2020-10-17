import sys
import subprocess
import unittest

from tests.utils.MessageFileReaderTests import MessageFileReaderTests
from tests.utils.DataLoaderFactoryTests import DataLoaderFactoryTests


def add_message_file_reader_tests(test_suite):
    test_suite.addTests([
        MessageFileReaderTests('test_should_generate_message_dict'),
        MessageFileReaderTests('test_should_raise_io_erorr')
    ])


def add_data_loader_factory_tests(test_suite):
    test_suite.addTests(
        [DataLoaderFactoryTests('test_should_return_correct_dictionary')])


def run_test_suite():

    test_runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
    """
    Add tests Module wise
    """
    add_message_file_reader_tests(test_suite)
    add_data_loader_factory_tests(test_suite)

    test_runner.run(test_suite)


if __name__ == "__main__":

    input_file_path = sys.argv[1]

    run_test_suite()

    subprocess.run("python -m geektrust " + input_file_path)
