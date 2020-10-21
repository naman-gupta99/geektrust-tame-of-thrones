import unittest

from main.services.southeros_ruler_services import *
from main.utils.southeros_ruler_service_factory import get_southeros_ruler_service


class SoutherosRulerServiceFactoyTests(unittest.TestCase):
    def test_should_return_messages_impl(self):
        """
        Check if factory returns correct instance
        """
        service = get_southeros_ruler_service('messages')()

        self.assertIsInstance(
            service, southeros_ruler_service_by_messages_impl.
            SoutherosRulerServiceByMessagesImpl)
