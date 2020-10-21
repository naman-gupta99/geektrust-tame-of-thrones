import sys
import subprocess
import unittest

from tests.models import *
from tests.controllers import *
from tests.repositoryservices.kingdom_repository_services import *
from tests.services.kingdom_data_services import *
from tests.services.southeros_ruler_services import *
from tests.utils import *


def add_cipher_factory_tests(test_suite):
    test_suite.addTests([
        test_cipher_factory.CipherFactoryTests(
            'test_should_return_seasar_cipher'),
        test_cipher_factory.CipherFactoryTests(
            'test_cipher_should_encrypt_plain_text'),
        test_cipher_factory.CipherFactoryTests(
            'test_cipher_should_decrypt_cipher_text')
    ])


def add_data_loader_factory_tests(test_suite):
    test_suite.addTests([
        test_data_loader_factory.DataLoaderFactoryTests(
            'test_should_return_correct_dictionary')
    ])


def add_kingdom_data_service_csv_impl_tests(test_suite):
    test_suite.addTests([
        test_kingdom_data_service_csv_impl.KingdomDataServiceCsvImplTests(
            'test_should_return_correct_kingdom_data')
    ])


def add_kingdom_data_service_factory_tests(test_suite):
    test_suite.addTests([
        test_kingdom_data_service_factory.KingdomDataServiceFactoryTests(
            'test_should_return_csv_impl')
    ])


def add_kingdom_repository_service_csv_impl_tests(test_suite):
    test_suite.addTests([
        test_kingdom_repository_service_csv_impl.
        KingdomRepositoryServicesCsvImplTests(
            'test_should_return_correct_data')
    ])


def add_kingdom_repository_service_factory_tests(test_suite):
    test_suite.addTests([
        test_kingdom_repository_service_factory.
        KingdomRepositoryServiceFactoryTests('test_should_return_csv_impl')
    ])


def add_kingdom_tests(test_suite):
    test_suite.addTests([
        test_kingdom.KingdomTests('test_should_create_correct_object'),
        test_kingdom.KingdomTests(
            'test_should_ally_on_recieving_correct_message'),
        test_kingdom.KingdomTests(
            'test_should_recieve_support_from_other_kingdom')
    ])


def add_message_file_reader_tests(test_suite):
    test_suite.addTests([
        test_message_file_reader.MessageFileReaderTests(
            'test_should_generate_message_dict'),
        test_message_file_reader.MessageFileReaderTests(
            'test_should_raise_io_erorr')
    ])


def add_ruler_tests(test_suite):
    test_suite.addTests(
        [test_ruler.RulerTests('test_should_create_correct_object')])


def add_southeros_ruler_controller_tests(test_suite):
    test_suite.addTests([
        test_southeros_ruler_controller.SoutherosRulerControllerTests(
            'test_should_return_ruler_kingdom_and_allies'
        ), test_southeros_ruler_controller.SoutherosRulerControllerTests(
            'test_should_return_none'
        )                
    ])


def add_southeros_ruler_service_by_messages_impl_tests(test_suite):
    test_suite.addTests([
        test_southeros_ruler_service_by_messages_impl.SoutherosRulerServiceByMessagesImplTests(
            'test_should_return_ruler'
        ), test_southeros_ruler_service_by_messages_impl.SoutherosRulerServiceByMessagesImplTests(
            'test_should_return_none'
        )
    ])


def add_southeros_ruler_service_factory_tests(test_suite):
    test_suite.addTests([
        test_southeros_ruler_service_factoy.SoutherosRulerServiceFactoyTests(
            'test_should_return_messages_impl')
    ])


def add_all_tests_to_suite(test_suite):
    """
    Add tests Module wise
    """
    add_cipher_factory_tests(test_suite)
    add_data_loader_factory_tests(test_suite)
    add_kingdom_data_service_csv_impl_tests(test_suite)
    add_kingdom_data_service_factory_tests(test_suite)
    add_kingdom_repository_service_csv_impl_tests(test_suite)
    add_kingdom_repository_service_factory_tests(test_suite)
    add_kingdom_tests(test_suite)
    add_message_file_reader_tests(test_suite)
    add_southeros_ruler_controller_tests(test_suite)
    add_southeros_ruler_service_by_messages_impl_tests(test_suite)
    add_southeros_ruler_service_factory_tests(test_suite)
    add_ruler_tests(test_suite)


def run_test_suite():

    test_runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
    add_all_tests_to_suite(test_suite)
    test_runner.run(test_suite)


if __name__ == "__main__":
    """
    Run all the test and then run the comaand to run the program
    """

    input_file_path = sys.argv[1]

    run_test_suite()

    subprocess.run("python -m geektrust " + input_file_path)