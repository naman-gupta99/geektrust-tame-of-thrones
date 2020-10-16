import sys
import subprocess
import unittest

from tests.utils.MessageFileReaderTests import MessageFileReaderTests


def run_test_suite():

    test_runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()

    test_suite.addTest(
        MessageFileReaderTests('test_should_generate_message_dict'))

    test_runner.run(test_suite)


if __name__ == "__main__":

    input_file_path = sys.argv[1]

    run_test_suite()

    subprocess.run("python -m geektrust " + input_file_path)
