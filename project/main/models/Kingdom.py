from globals.configs import CIPHER_TECHNIQUE
from main.utils.CipherFactory import get_cipher_util


class Kingdom:
    """
    Model to represent Kingdom
    """
    def __init__(self, name: str, emblem: str):
        """
        : name : Name of the Kingdom
        : emblem : Emblem of the Kingdom
        """

        self.__name = name
        self.__emblem = emblem
        self.__cipher = get_cipher_util(CIPHER_TECHNIQUE)()

    def send_message(self, reciever_kingdom, message: str) -> bool:
        """
        Send Message to the Reciever Kingdom and check if it is an ally
        : reciever_kingdom : Kingdom Object of the Kingdom to whom message is sent
        : message : String message to be sent to the other country

        Returns the response sent by the Reciever Kingdom
        """

        return reciever_kingdom.recieve_message(message)

    def recieve_message(self, message: str) -> bool:
        """
        Check if the message recived has the emblem after decryption
        : message : Recieved string message

        Returns if the kingdom can ally with the Sender kingdom
        """

        decrypted_message = self.__cipher.decrypt(message, len(self.__emblem))

        return self.check_emblem_in_message(decrypted_message)

    def check_emblem_in_message(self, message: str) -> bool:
        """
        Checks if all the letters of emblem are presnt in the message
        
        : message : Message recieved
        """

        emblem_dic = {}
        for ch in self.__emblem.upper():
            if ch in emblem_dic:
                emblem_dic[ch] += 1
            else:
                emblem_dic[ch] = 1

        for ch in message.upper():
            if ch in emblem_dic:
                emblem_dic[ch] -= 1
                if emblem_dic[ch] == 0:
                    del emblem_dic[ch]
        return len(emblem_dic) == 0

    def __eq__(self, other):
        return self.__name == other.get_name(
        ) and self.__emblem == other.get_emblem()

    def __str__(self):
        """
        Return String representation of the object
        """
        return self.__name + " " + self.__emblem

    """
    Getters and Setters
    """

    def get_name(self):
        return self.__name

    def get_emblem(self):
        return self.__emblem