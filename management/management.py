from mongoengine import *
from datetime import datetime
import hashlib, uuid
#    mongod --noauth --dbpath . --port 27777

port=27777

def IMPLEMENT():
    print "IMPLEMENT ME"

def generate_password_hash(password)
    # maybe using passlib https://pypi.python.org/pypi/passlibx
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    return hashed_password
    
class User(Document):
    """This class is sued to represent a user"""
    title = StringField("")
    firstname = StringField()
    lastname = StringField()
    email = EmailField()
    active = BooleanField()
    password = StringField()
    userid = UUIDField()
    date_modified = DateTimeField(default=datetime.now)

    def activate (self):
        activate = True

    def deactivate (self):
        activate = False
            
    def set_password(self, password):
        #self.password_hash = generate_password_hash(password)
        pass
        
    def check_password(self, password):
        #return check_password_hash(self.password_hash, password)
        pass
        
    def to_json(self):
        """prints the user as a json object"""
        return {
            "title" : self.title,
            "firstname" : self.firstname,
            "lastname" :  self.lastname,
            "email" : self.email,
            "active" : self.active,
            "password" : self.password,
            "userid" : self.userid,
            "date_modified" : self.date_modified,
            }

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.title,self.firstname, self.lastname, self.email)

class Users(object):

    def __init__(self):
        db = connect('user', port=port)
        users = User.objects()
    
    def add(self, user):
        """adds the specified user to mongodb"""
        if self.verify(user):
            user.save()
        else:
            print "ERROR: a user with the e-mail `{0}` already exists".format(user.email)
            
    def verify(self, user):
        """verifies if the user can be added. Checks if the e-mail is unique. Returns true."""
        _user = User.objects(email=user.email)
        return _user.count == 0

    def get(self, email):
        """find the user with the given email and return its json object"""
        IMPLEMENT()

    def find(self, email):
        """returns the users based on the give query"""
        found = User.objects(email=email)
        if found.count() > 0:
            return found[0].to_json()
        else:
            return None

    def clean(self):
        """removes all elements form the mongo db that are users"""
        IMPLEMENT()

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
    


def main():

    users = Users()
    users.clean()
    
    gregor = User(
        title = "",
        firstname = "Gregor",
        lastname = "von Laszewski",
        email = "laszewski@gmail.com",
        active = True,
        password = "none"
    )
    users.add(gregor)

    print users.find("laszewski@gmail.com")
    
    


if __name__ == "__main__":
    main()
