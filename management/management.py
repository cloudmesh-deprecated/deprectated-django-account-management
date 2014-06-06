from mongoengine import *

connect ('user')

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
    
    jeff = User(title = "Mr.", firstname = "Jeffery", 
                   lastname = "Ridgeway", 
                   email = "jeff01@gmail.com")
    jeff.save()
    
    account = Account(username = "jeff01",
                      email = "jeff01@gmail.com",
                      password = "17JEFF1992")
    account.owner = jeff
    account.save()
    
    print
    print "LIST OBJECTS"
    print 70 * "-"
    print

    accounts = Account.objects()

    for account in accounts:
        print account.owner.firstname, ":", account

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
    

    
