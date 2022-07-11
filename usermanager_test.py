feature/updateuser
import unittest
from user_manager import Usermanager
from user import User

class UserManagerTest(unittest.TestCase):
    def test_addUser(self):
        user_manager=Usermanager()
        user1 = User("Rincy", "r@r.com,", 11, "Delhi")
        user_manager.addUser(user1)
        self.assertTrue(len(user_manager.users)>0)

    def test_removeuser(self):
        user_manager=Usermanager()
        aNewUser=User("Rincy", "r@r.com,", 11, "Delhi")
        user_manager.addUser(aNewUser)
        users_size = len(user_manager.users)
        print(f"valid added for remove test:{len{users_size}")
        
        user_manager.removeUser(0)
        print(f"user removed added:{len(user_manager.users)}")
        self.assertTrue(len(user_manager.users)==users_size-1)




if __name__ == '__main__':
    unittest.main()

import unittest
from user_manager import Usermanager
from user import User

class UserManagerTest(unittest.TestCase):
    def test_addUser(self):
        user_manager=Usermanager()
        user1 = User("Rincy", "r@r.com,", 11, "Delhi")
        user_manager.addUser(user1)
        self.assertTrue(len(user_manager.users)>0)

    def test_removeuser(self):
        user_manager=Usermanager()
        aNewUser=User("Rincy", "r@r.com,", 11, "Delhi")
        user_manager.addUser(aNewUser)
        users_size = len(user_manager.users)
        print(f"valid added for remove test:{len{users_size}")
        
        user_manager.removeUser(0)
        print(f"user removed added:{len(user_manager.users)}")
        self.assertTrue(len(user_manager.users)==users_size-1)




if __name__ == '__main__':
    unittest.main()

        