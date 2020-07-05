import unittest

from Holiday.holiday import say_hello


class HolidayTests(unittest.TestCase):
    def test_today_is_xmas(self):
        self.assertEqual("Merry Xmas", say_hello())


if __name__ == '__main__':
    unittest.main()
