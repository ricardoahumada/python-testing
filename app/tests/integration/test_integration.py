import unittest
import json
from types import SimpleNamespace

from my_app import App


class Mock_Database:
    path = ''

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, 'r') as f:
            data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
        # print(data)
        return data

# Copied from realpython.com for example - won't run


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database=Mock_Database('tests/integration/fixtures/test_basic.json'))

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "Emmey")
        self.assertEqual(customer.address, "97574 Nevada Junction")


class TestComplexData(unittest.TestCase):
    def setUp(self):
        # load test data
        self.app = App(database=Mock_Database('tests/integration/fixtures/test_complex.json'))

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 1000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=999)
        self.assertEqual(customer.first_name, u"バナナ")
        self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")


if __name__ == '__main__':
    unittest.main()
