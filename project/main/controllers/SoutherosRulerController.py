import os

from globals.configs import DATA_LOADING_SOURCE, RULER_CHECKING_CONDITION
from main.services.SoutherosRulerServices import *
from main.utils.MessageFileReader import read_messages_from_file
from main.utils.KingdomDataServiceFactory import get_kingdom_data_service
from main.utils.SoutherosRulerServiceFactory import get_southeros_ruler_service


class SoutherosRulerController:
    def __init__(self):
        """
        Initialize Controller object with a Service Object
        """
        self.southeros_ruler_service = get_southeros_ruler_service(
            RULER_CHECKING_CONDITION)()

    def check_if_space_is_ruler_using_input_file(self, file_path: str) -> str:
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

        ruler = self.southeros_ruler_service.check_ruler_of_southeros(
            "SPACE", messages)

        if ruler == None:
            return "NONE"
        else:
            return str(ruler)
