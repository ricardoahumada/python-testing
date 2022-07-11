import unittest
from user_manager import UserManager
from user import User

class UserManagerTest(unittest.TestCase):
    def test_addUser(self):
        user_manager=UserManager()
        aNewUser=User("Juan","j@j.com",34,"Lonsodn street")

        print(f"before: {len(user_manager.users)}")

        user_manager.addUser(aNewUser)
        print(f"valid added: {len(user_manager.users)}")
        
        self.assertTrue(len(user_manager.users)>0)

        user_manager.addUser(None)
        print(f"1 invalid added: {len(user_manager.users)}")        
        self.assertTrue(len(user_manager.users)==1)

        user_manager.addUser(User(None, None,0,None))
        print(f"2 invalid added: {len(user_manager.users)}")        
        self.assertTrue(len(user_manager.users)==1)


if __name__ == '__main__':
    unittest.main()
