import unittest
from datetime import date
from unittest.mock import patch

from Holiday.holiday import say_hello


class HolidayTests(unittest.TestCase):
    def test_today_is_xmas(self):
        self.fake_get_today.return_value = date(2020, 12, 25)
        self.assertEqual("Merry Xmas", say_hello())

    def setUp(self) -> None:
        get_today_patcher = patch('Holiday.holiday.__get_today')
        self.fake_get_today = get_today_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()


if __name__ == '__main__':
    unittest.main()
