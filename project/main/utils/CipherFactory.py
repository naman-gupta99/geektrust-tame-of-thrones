from main.utils.ciphers import *


def get_cipher_util(cipher_technique):
    """
    Returns class of Cipher
    : cipher_technique : Name of cipher to be used
    """

    if cipher_technique == "Seasar":
        return SeasarCipherUtil.SeasarCipherUtil
    else:
        raise NotImplementedError('Cipher Util of type "' + cipher_technique +
                                  '" not implemented')
