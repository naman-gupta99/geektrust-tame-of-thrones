import os

from globals.configs import RULER_CHECKING_CONDITION
from main.utils.message_file_reader import read_messages_from_file
from main.utils.southeros_ruler_service_factory import get_southeros_ruler_service


class SoutherosRulerController:
    def __init__(self):
        """
        Initialize Controller object with a Service Object
        """
        self.__southeros_ruler_service = get_southeros_ruler_service(
            RULER_CHECKING_CONDITION)()

    def check_if_kingdom_is_ruler_using_input_file(self, kingdom_name:str, file_path: str) -> str:
        """
        Controller to accept the request

        - Uses Message Reading util to read messages
        - Uses service to find the output
        - Returns in the Suitable format

        : file_path : Absolute path to the input file 
        """

        if not os.path.isfile(file_path):
            raise FileNotFoundError('"' + file_path + '" is not a valid path')

        messages = read_messages_from_file(file_path)

        ruler = self.__southeros_ruler_service.check_ruler_of_southeros(
            kingdom_name, messages)

        if ruler == None:
            return "NONE"
        else:
            return str(ruler)
