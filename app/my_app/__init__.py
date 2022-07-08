import os

class CustomerManager:
    customers = None

    def get_customer(self, id):
        for item in self.customers:
            if item.id == id:
                # print(item)
                return item
        return None


def App(database):
    customerManager = CustomerManager()
    customerManager.customers = database.load_data()
    return customerManager
