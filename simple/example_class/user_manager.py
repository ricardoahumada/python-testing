from user import User

class UserManager:
    users=[]

    def addUser(self,newUser):
        if newUser != None and newUser.name!=None and newUser.email!=None and newUser.address!=None and newUser.age!=0:
            self.users.append(newUser)
