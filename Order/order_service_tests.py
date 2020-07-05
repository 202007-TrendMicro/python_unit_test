import unittest
from unittest.mock import patch

from testfixtures import compare

from Order.order_service import OrderService, Order


class OrderServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.order_service = OrderService()
        get_orders_patcher = patch('Order.order_service.OrderService.get_orders')
        self.fake_get_orders = get_orders_patcher.start()
        insert_patcher = patch('Order.order_service.BookDao.insert')
        self.fake_insert = insert_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()

    def test_only_2_book_orders_in_3_orders_when_sync_book_orders(self):
        self.given_orders([
            Order(order_type="Book", price=100),
            Order(order_type="CD"),
            Order(order_type="Book", price=200),
        ])

        self.when_sync_book_order()

        self.should_insert_order_count(2)
        self.first_inserted_order_should_be(Order(order_type="Book", price=100))
        self.second_inserted_order_should_be(Order(order_type="Book", price=200))

    def second_inserted_order_should_be(self, expected):
        second_order = self.fake_insert.call_args_list[1].args[0]
        compare(expected, second_order)

    def first_inserted_order_should_be(self, expected):
        first_order = self.fake_insert.call_args_list[0].args[0]
        compare(expected, first_order)

    def should_insert_order_count(self, times):
        self.assertEqual(times, self.fake_insert.call_count)

    def when_sync_book_order(self):
        self.order_service.sync_book_orders()

    def given_orders(self, orders):
        self.fake_get_orders.return_value = orders


if __name__ == '__main__':
    unittest.main()
