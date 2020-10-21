from main.repository_services.kingdom_repository_services import *


def get_kingdom_repository_service(source_type):
    """
    Returns class of Kingdom Repository Service
    : source_type : Type of repository source
    """
    if source_type == "csv":
        return kingdom_repository_service_csv_impl.KingdomRepositoryServiceCsvImpl
    else:
        raise NotImplementedError(
            'Kingdom Repository Service with source type "' + source_type +
            '" not implemented')
