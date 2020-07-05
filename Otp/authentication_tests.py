import unittest
from unittest.mock import patch

from Otp.authentication_service import is_valid


class AuthenticationServiceTests(unittest.TestCase):
    def test_is_valid(self):
        self.given_password("91")
        self.given_otp("000000")
        self.should_be_valid("joey", "91000000")

    def test_is_invalid(self):
        self.given_password("91")
        self.given_otp("000000")
        self.should_be_invalid("joey", "wrong password")

    def should_be_invalid(self, account, password):
        self.assertEqual(False, is_valid(account, password))

    def should_be_valid(self, account, password):
        self.assertEqual(True, is_valid(account, password))

    def given_otp(self, otp):
        self.fake_get_otp.return_value = otp

    def given_password(self, password):
        self.fake_get_password.return_value = password

    def setUp(self) -> None:
        get_password_patcher = patch('Otp.authentication_service.get_password_from_db')
        self.fake_get_password = get_password_patcher.start()
        get_otp_patcher = patch('Otp.authentication_service.get_otp')
        self.fake_get_otp = get_otp_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()


if __name__ == '__main__':
    unittest.main()
