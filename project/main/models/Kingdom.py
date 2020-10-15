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

        self.name = name
        self.emblem = emblem
        self.cipher = get_cipher_util(CIPHER_TECHNIQUE)()

    def send_message(self, reciever_kingdom, message: str) -> bool:
        """
        Send Message to the Reciever Kingdom and check if it is an ally
        : reciever_kingdom : Kingdom Object of the Kingdom to whom message is sent
        : message : String message to be sent to the other country
        """

        return reciever_kingdom.recieve_message(message)

    def recieve_message(self, message: str) -> bool:
        """
        Check if the message recived has the emblem after decryption
        : message : Recieved string message
        """

        decrypted_message = self.cipher.decrypt(message, len(self.emblem))

        return self.check_emblem_in_message(decrypted_message)

    def check_emblem_in_message(self, message: str) -> bool:

        emblem_dic = {}
        for ch in self.emblem.upper():
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

    def __str__(self):
        """
        Return String representation of the object
        """
        return self.name + " " + self.emblem
