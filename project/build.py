import sys
import subprocess
import unittest

from tests.utils.DataLoaderFactoryTests import DataLoaderFactoryTests
from tests.utils.KingdomDataServiceFactoryTests import KingdomDataServiceFactoryTests
from tests.utils.KingdomRepositoryServiceFactoryTests import KingdomRepositoryServiceFactoryTests
from tests.utils.MessageFileReaderTests import MessageFileReaderTests
from tests.utils.SoutherosRulerServiceFactoyTests import SoutherosRulerServiceFactoyTests


def add_message_file_reader_tests(test_suite):
    test_suite.addTests([
        MessageFileReaderTests('test_should_generate_message_dict'),
        MessageFileReaderTests('test_should_raise_io_erorr')
    ])


def add_data_loader_factory_tests(test_suite):
    test_suite.addTests(
        [DataLoaderFactoryTests('test_should_return_correct_dictionary')])


def add_kingdom_data_service_factory_tests(test_suite):
    test_suite.addTests(
        [KingdomDataServiceFactoryTests('test_should_return_csv_impl')])


def add_kingdom_repository_service_factory_tests(test_suite):
    test_suite.addTests(
        [KingdomRepositoryServiceFactoryTests('test_should_return_csv_impl')])


def add_southeros_ruler_service_factory_tests(test_suite):
    test_suite.addTests(
        [SoutherosRulerServiceFactoyTests('test_should_return_messages_impl')])


def run_test_suite():

    test_runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
    """
    Add tests Module wise
    """
    add_message_file_reader_tests(test_suite)
    add_data_loader_factory_tests(test_suite)
    add_kingdom_data_service_factory_tests(test_suite)
    add_kingdom_repository_service_factory_tests(test_suite)
    add_southeros_ruler_service_factory_tests(test_suite)

    test_runner.run(test_suite)


if __name__ == "__main__":

    input_file_path = sys.argv[1]

    run_test_suite()

    subprocess.run("python -m geektrust " + input_file_path)
