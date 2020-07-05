import csv


class Order(object):

    def __init__(self, product_name, order_type, price, customer_name):
        self.customer_name = customer_name
        self.price = price
        self.type = order_type
        self.product_name = product_name


class BookDao(object):
    def insert(self, book_order):
        raise NotImplementedError


class OrderService(object):

    def __init__(self):
        self.order_path = '/source/testOrders.csv'

    def sync_book_orders(self):
        orders = self.get_orders()
        book_orders = list(filter(lambda o: (o.type == 'Book'), orders))
        book_dao = BookDao()
        for book_order in book_orders:
            book_dao.insert(book_order)

    def get_orders(self) -> list:
        my_list = []
        with open(self.order_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                my_list.append(Order(row[0], row[1], row[2], row[3]))

        return my_list
