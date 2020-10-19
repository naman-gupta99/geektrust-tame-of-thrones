from main.services.southeros_ruler_services import *


def get_southeros_ruler_service(condition_type):
    """
    Returns class of Southeros Ruler Service
    : condition_type : Condition to be used to get the Ruler
    """
    if condition_type == "messages":
        return southeros_ruler_service_by_messages_impl.SoutherosRulerServiceByMessagesImpl
    else:
        raise NotImplementedError(
            'Southeros Ruler Service with condition type "' + condition_type +
            '" not implemented')
