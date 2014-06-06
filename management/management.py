from mongoengine import *

#    mongod --noauth --dbpath . --port 27777

class User(Document):
    title = StringField()
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    
    def __str__(self):
        return "{0} {1} {2} {3}".format(self.title,self.firstname, self.lastname, self.email)
        
class Account(Document):
    owner = ReferenceField(User)
    username = StringField()
    email = StringField()
    password = StringField()
    
    def __str__(self):
        return "{0} {1}".format(self.owner,self.username)
    
    
class Contact(Document):
    PhoneNumber = StringField()    
    Department = StringField()
    Institution = StringField()
    Adviser_Contact_Info = StringField()
    Inst_Address = StringField()
    Insitution_Country = StringField()
    url = StringField()
    Citizenship = StringField()
    Bio = StringField()
    SignUp_Code = StringField()








