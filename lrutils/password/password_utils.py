# all this shamelessly ripped off from flask-security plugin cause it was well done over there

import base64
import hashlib
import hmac

from passlib.context import CryptContext

class PasswordUtils(object):

    def __init__(self, config):
        self.salt = config.get('SECURITY_PASSWORD_SALT', None)
        self.pw_hash = config.get('SECURITY_PASSWORD_HASH', None)

        if self.salt is None:
            raise RuntimeError("The configuration value 'SECURITY_PASSWORD_SALT' must be set")

        if self.pw_hash is None:
            raise RuntimeError("The configuration value 'SECURITY_PASSWORD_HASH' must be set")

        self.pwd_context = CryptContext(schemes=[self.pw_hash])


    def get_hmac(self, password):
        h = hmac.new(self.encode_string(self.salt), self.encode_string(password), hashlib.sha512)
        return base64.b64encode(h.digest())


    def encrypt_password(self, password):
        signed = self.get_hmac(password).decode('ascii')
        return self.pwd_context.encrypt(signed)


    def verify_password(self, password, password_hash):
        password = self.get_hmac(password)
        return self.pwd_context.verify(password, password_hash)


    def encode_string(self, string):
        if isinstance(string, unicode):
            string = string.encode('utf-8')
        return string

