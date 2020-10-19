from main.services.kingdom_data_services import *


def get_kingdom_data_service(source_type):
    """
    Returns class of Kingdom Data Service
    : source_type : Type of repository source
    """
    if source_type == "csv":
        return kingdom_data_service_csv_impl.KingdomDataServiceCsvImpl
    else:
        raise NotImplementedError('Kingdom Data Service with source type "' +
                                  source_type + '" not implemented')
