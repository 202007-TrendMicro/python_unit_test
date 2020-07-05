import unittest
from unittest.mock import patch

from testfixtures import compare

from Order.order_service import OrderService, Order


class OrderServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        get_orders_patcher = patch('Order.order_service.OrderService.get_orders')
        self.fake_get_orders = get_orders_patcher.start()
        insert_patcher = patch('Order.order_service.BookDao.insert')
        self.fake_insert = insert_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()

    def test_only_2_book_orders_in_3_orders_when_sync_book_orders(self):
        self.fake_get_orders.return_value = [
            Order(order_type="Book", price=100),
            Order(order_type="CD"),
            Order(order_type="Book", price=200),
        ]

        order_service = OrderService()
        order_service.sync_book_orders()

        self.assertEqual(2, self.fake_insert.call_count)
        first_order = self.fake_insert.call_args_list[0].args[0]
        compare(Order(order_type="Book", price=100), first_order)
        second_order = self.fake_insert.call_args_list[1].args[0]
        compare(Order(order_type="Book", price=200), second_order)


if __name__ == '__main__':
    unittest.main()
