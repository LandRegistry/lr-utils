import unittest

from password import PasswordUtils

class PasswordUtilsTestCase(unittest.TestCase):


    def test_password_hash_verifies(self):

        config = {'SECURITY_PASSWORD_SALT' :  'no-secret',  'SECURITY_PASSWORD_HASH' : 'bcrypt'}
        pass_util = PasswordUtils(config)

        self.assertTrue( pass_util.verify_password('dummy', pass_util.encrypt_password('dummy')) )
        self.assertFalse( pass_util.verify_password('dumbass', pass_util.encrypt_password('dummy')) )


    def test_salt_must_be_in_config(self):
        config = {'SECURITY_PASSWORD_SALT' :  None,  'SECURITY_PASSWORD_HASH' : 'bcrypt'}
        self.assertRaisesRegexp(RuntimeError, "The configuration value 'SECURITY_PASSWORD_SALT' must be set",  PasswordUtils, config)


    def test_hash_must_be_in_config(self):
        config = {'SECURITY_PASSWORD_SALT' :  'no-secret',  'SECURITY_PASSWORD_HASH' : None}
        self.assertRaisesRegexp(RuntimeError, "The configuration value 'SECURITY_PASSWORD_HASH' must be set",  PasswordUtils, config)

