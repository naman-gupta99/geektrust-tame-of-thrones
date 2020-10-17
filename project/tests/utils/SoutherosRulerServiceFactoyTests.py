import unittest

from main.services.SoutherosRulerServices import *
from main.utils.SoutherosRulerServiceFactory import get_southeros_ruler_service


class SoutherosRulerServiceFactoyTests(unittest.TestCase):
    def test_should_return_messages_impl(self):

        service = get_southeros_ruler_service('messages')()

        self.assertIsInstance(
            service, SoutherosRulerServiceByMessagesImpl.
            SoutherosRulerServiceByMessagesImpl)
