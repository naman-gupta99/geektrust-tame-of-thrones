from main.repositoryservices.KingdomRepositoryServices import *


def get_kingdom_repository_service(source_type):
    """
    Returns class of Kingdom Repository Service
    : source_type : Type of repository source
    """
    if source_type == "csv":
        return KingdomRepositoryServiceCsvImpl.KingdomRepositoryServiceCsvImpl
    else:
        raise NotImplementedError(
            'Kingdom Repository Service with source type "' + source_type +
            '" not implemented')
