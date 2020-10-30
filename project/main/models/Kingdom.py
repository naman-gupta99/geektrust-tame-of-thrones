from globals.configs import CIPHER_TECHNIQUE
from main.utils.cipher_factory import get_cipher_util


class Kingdom:
    """
    Model to represent Kingdom
    """
    def __init__(self, name: str, emblem: str, allies=[]):
        """
        : name : Name of the Kingdom
        : emblem : Emblem of the Kingdom
        : allies : List of Allies
        """

        self.__name = name
        self.__emblem = emblem
        self.__cipher = get_cipher_util(CIPHER_TECHNIQUE)()
        self.__allies = allies

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

    def evaluate_allies(self, kingdoms: dict, messages: dict) -> None:

        self.__allies = []

        for kingdom_name in messages:
            if kingdom_name != self.__name:
                if kingdom_name in kingdoms:
                    for message in messages[kingdom_name]:
                        if self.send_message(kingdoms[kingdom_name],
                                                 message):
                            self.__allies.append(kingdoms[kingdom_name])
                            break

    def __eq__(self, other):
        """
        Override Equality
        """

        if not type(self) is type(other):
            return False

        if self.__name != other.get_name():
            return False
        if self.__emblem != other.get_emblem():
            return False
        return True

    def __str__(self):
        """
        Return String representation of the object
        """
        return self.__name + " " + ' '.join([ally.get_name() for ally in self.__allies])

    """
    Getters and Setters
    """

    def get_name(self):
        return self.__name

    def get_emblem(self):
        return self.__emblem

    def get_allies(self):
        return self.__allies