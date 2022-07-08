import unittest

from my_app import App

# Copied from realpython.com for example - won't run
class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='tests/integration/fixtures/test_basic.json')

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
        self.app = App(database='tests/integration/fixtures/test_complex.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 1000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=999)
        self.assertEqual(customer.first_name, u"バナナ")
        self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")

if __name__ == '__main__':
    unittest.main()