from mongoengine import *

#    mongod --noauth --dbpath . --port 27777

port=27777

class User(Document):
    """This class is sued to represent a user"""
    title = StringField()
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    active = BooleanField()
    #password = ???

    def to_json(self):
        """prints the user as a json object"""
        return {}

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.title,self.firstname, self.lastname, self.email)

class Users(Object):

    def __init__(self):
        db = connect('user', port=port)
        users = User.Objects()
    
    def add(self):
        """adds the specified user to mongodb"""
        if self.verify():
            print "IMPLEMENT ME"
        else:
            print "ERROR: a user with this the e-mail already exists"
            
    def verify(self):
        """verifies if the user can be added. Checks if the e-mail is unique. Returns true."""
        print "IMPLEMENT ME"
        return false

    def get(self, email):
        """find the user with the given email and return its json object"""
        print "IMPLEMENT ME"

    def find(self, query):
        """returns the users based on the give query"""
        print "implement me"
        # return the json object
    
                    
class Account(Document):
    owner = ReferenceField(User)
    #projects = StringField() 
    username = StringField()
    email = StringField()
    password = StringField()
    phone = StringField()
    department = StringField()
    institution = StringField()
    adviser_contact = StringField()
    institute_address = StringField()
    institute_country = StringField()
    url = StringField()
    citizenship = StringField()
    bio = StringField()
    signup_code = StringField()
    
    _order = [
            "owner",
            "username",
            "email",
            "phone",
            "department",
            "institution",
            "adviser_contact",
            "institute_address",
            "institute_country",
            "url",
            "citizenship",
            "bio",
            "signup_code"
    ]
    
    def to_json(self):
        u = {"owner":self.owner,
            "username":self.username,
            "email":self.email,
            "phone":self.phone,
            "department":self.department,
            "institution":self.institution,
            "adviser_contact":self.adviser_contact,
            "institute_address":self.institute_address,
            "institute_country":self.institute_country,
            "url":self.url,
            "citizenship":self.citizenship,
            "bio":self.bio,
            "signup_code":self.signup_code}
        return u

    
    def __str__(self):
        u = self.to_json()
        return str(u)
        

#class Contact(Document):
    






