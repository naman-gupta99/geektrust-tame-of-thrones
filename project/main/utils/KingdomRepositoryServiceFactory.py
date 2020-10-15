from main.repositoryservices.KingdomRepositoryServices import *


def get_kingdom_repository_service(source_type):

    if source_type == "csv":
        return KingdomRepositoryServiceCsvImpl.KingdomRepositoryServiceCsvImpl
    else:
        raise NotImplementedError(
            'Kingdom Repository Service with source type "' + source_type +
            '" not implemented')
