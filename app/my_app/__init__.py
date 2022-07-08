import json
import os
from types import SimpleNamespace

class CustomerManager:
    customers = []

    def get_customer(self, id):
        for item in self.customers:
            if item.id == id:
                # print(item)
                return item
        return None


def App(database):
    customerManager = CustomerManager()
    directory = os.getcwd()
    print(directory)
    with open(database, 'r') as f:
        data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    # print(data)

    customerManager.customers = data
    return customerManager
