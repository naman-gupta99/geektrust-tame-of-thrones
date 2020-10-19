import abc


class CipherUtil(metaclass=abc.ABCMeta):
    """
    Cipher Utility Interface to build a Cipher Utility to Encrypt and Decrypt a message
    """

    @abc.abstractmethod
    def decrypt(self, cipher_text: str, key) -> str:
        """
        Decrypt the cipher_text
        Return Plain Text
        """

        pass

    @abc.abstractmethod
    def encrypt(self, plain_text: str, key) -> str:
        """
        Encrypt plain_text using a Cipher Technique
        Return Cipher text
        """

        pass