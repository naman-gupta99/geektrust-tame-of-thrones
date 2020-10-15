from main.services.SoutherosRulerServices import *


def get_southeros_ruler_service(condition_type):

    if condition_type == "messages":
        return SoutherosRulerServiceByMessagesImpl.SoutherosRulerServiceByMessagesImpl
    else:
        raise NotImplementedError(
            'Southeros Ruler Service with condition type "'
            + condition_type
            + '" not implemented'
        )