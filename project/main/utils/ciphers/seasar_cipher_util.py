from main.utils.ciphers.cipher_util import CipherUtil


class SeasarCipherUtil(CipherUtil):
    """
    Seasar Cipher Class: encrypts Plain text by changing every alphabet with an alphabet key places
    ahead.
    """
    def encrypt(self, plain_text: str, key: int) -> str:
        """
        Encrypt the plain_text
        return cipher_text
        """
        cipher_text = ""
        for i in plain_text:
            if i.isalpha():
                if i.isupper():
                    cipher_text += chr((ord(i) - ord("A") + key) % 26 +
                                       ord("A"))
                else:
                    cipher_text += chr((ord(i) - ord("a") + key) % 26 +
                                       ord("a"))
            else:
                cipher_text += i

        return cipher_text

    def decrypt(self, cipher_text: str, key: int) -> str:
        """
        Decrypt the plain_text
        return plain_text
        """
        plain_text = ""
        for i in cipher_text:
            if i.isalpha():
                if i.isupper():
                    plain_text += chr((ord(i) - ord("A") - key) % 26 +
                                      ord("A"))
                else:
                    plain_text += chr((ord(i) - ord("a") - key) % 26 +
                                      ord("a"))
            else:
                plain_text += i

        return plain_text