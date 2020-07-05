import unittest
from unittest.mock import patch

from Otp.authentication_service import is_valid


class AuthenticationServiceTests(unittest.TestCase):
    def test_is_valid(self):
        self.fake_get_password.return_value = "91"
        self.fake_get_otp.return_value = "000000"
        self.assertEqual(True, is_valid("joey", "91000000"))

    def setUp(self) -> None:
        get_password_patcher = patch('Otp.authentication_service.get_password_from_db')
        self.fake_get_password = get_password_patcher.start()
        get_otp_patcher = patch('Otp.authentication_service.get_otp')
        self.fake_get_otp = get_otp_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()


if __name__ == '__main__':
    unittest.main()
