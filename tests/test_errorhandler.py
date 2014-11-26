import unittest
from flask import Flask, abort
from lrutils.errorhandler.errorhandler_utils import eh_after_request
from lrutils.errorhandler.errorhandler_utils import ErrorHandler

class ErrorHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask('tests')
        ErrorHandler(self.app)
        self.client = self.app.test_client()

    def test_headers(self):
        response = self.app.make_response("error.html")

        eh_after_request(response)
        assert response.headers.get('Content-Security-Policy')
        assert response.headers.get('X-Frame-Options')
        assert response.headers.get('X-Content-Type-Options')
        assert response.headers.get('X-XSS-Protection')
