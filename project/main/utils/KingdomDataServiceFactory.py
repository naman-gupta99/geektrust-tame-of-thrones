from main.services.KingdomDataServices import *


def get_kingdom_data_service(source_type):

    if source_type == "csv":
        return KingdomDataServiceCsvImpl.KingdomDataServiceCsvImpl
    else:
        raise NotImplementedError('Kingdom Data Service with source type "' +
                                  source_type + '" not implemented')
