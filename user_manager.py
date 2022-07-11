from user import User
class Usermanager:
    users=[]
   
    def addUser(self, newUser):
        if  newUser != None and newUser.name != None 
        and newUser.email!=None and newUser.age!=0:
        self.users.append(newUser)

    def removeUser(self, position):
        if len(self.users)>0:
         self.users.remove(position)
        
