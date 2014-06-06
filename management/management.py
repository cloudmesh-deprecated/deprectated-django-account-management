from mongoengine import *

connect ('user')

class User(Document):
    title = StringField()
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    
    def __str__(self):
        return "".format(self.title,self.firstname, self.lastname, self.email)
    
    
        
class Account(Document):
    owner = ReferenceField(User)
    username = StringField()
    email = StringField()
    password = StringField()
    
    def __str__(self):
        return "{0} {1}".format(self.owner,self.username, self.email, self.password)
    
    
class ContactInfo(Document):
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

    ifeanyi = User(title = "Mr.", firstname = "Ifeanyi", 
                   lastname = "Onyenweaku", 
                   email = "rowlandifeanyi17@gmail.com")
    ifeanyi.save()
    
    account = Account(username = "rowlandifeanyi",
                      email = "rowlandifeanyi17@gmail.com",
                      password = "17ROW1992")
    account.owner = ifeanyi
    account.save()
    
    print
    print "LIST OBJECTS"
    print 70 * "-"
    print

    accounts = Account.objects(owner = ifeanyi)

    for account in accounts:
        print account.owner, ":", account

    print
    print 70 * "-"
    
    







"""class Project


281
929936
    def __init__()

        
class Role

    def __init__():
        pass

    def add(role):
        pass
    
    def list():
        returns an array of roles
"""        
    

    
