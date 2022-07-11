from turtle import update
from unicodedata import name

class User:
    name = None
    email = None
    age = 0
    address = None

    def __init__(self, namev, emailv,agev, addressv) -> None:
        self.name = namev
        self.email = emailv
        self.age = agev
        self.address = addressv
        
    def talk(self):
        return f"Hello, I am a user and my name is {self.name}"

    def saysAddress(self):
        return f"Good morning, my address is {self.address}"

    def updateAge(self):
        return f"my age is {self.age}"



    