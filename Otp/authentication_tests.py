import unittest

from Otp.authentication_service import is_valid


class AuthenticationServiceTests(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(True, is_valid("joey", "91000000"))


if __name__ == '__main__':
    unittest.main()
