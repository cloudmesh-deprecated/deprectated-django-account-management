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

    #
    # User Information
    #
    username = StringField()
    
    title = StringField("")
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    email = EmailField(required=True)
    url = StringField()
    citizenship = StringField(required=True)
    bio = StringField(required=True)
    password = StringField(required=True)
    userid = UUIDField()
    active = BooleanField() # and data of now is less date deactivate
    phone = StringField(required=True)

    #owner = ReferenceField(User)
    #projects = StringField() 
    #
    # Affiliation
    #
    institution = StringField(required=True)
    department = StringField(required=True)
    address = StringField(required=True)
    country = StringField(required=True)
    adviser_contact = StringField()
    # advisor = pointer to another user
    

    date_modified = DateTimeField(default=datetime.now)
    date_created = DateTimeField(default=datetime.now)
    date_approved = None 
    date_deactivate = None # put date created + 6 month

    def is_active(self):
        # find if user is in active project
        #if self.active and date_deactivate > datetime.now
        #   retrun True
        #else
        #   return false   
        return True

        
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
            #"username":self.username,
            #"phone":self.phone,
            #"department":self.department,
            #"institution":self.institution,
            #"adviser_contact":self.adviser_contact,
            #"institute_address":self.institute_address,
            #"institute_country":self.institute_country,
            #"url":self.url,
            #"citizenship":self.citizenship,
            #"bio":self.bio,
            #"signup_code":self.signup_code}

        }

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.title,self.firstname, self.lastname, self.email)

class Users(object):

    def __init__(self):
        db = connect('user', port=port)
        self.users = User.objects()

    def objects(self)
        return self.users
    
    def set_username(self, proposal):
        """sets the username to the proposed username. if this name is taken, a

        number is added and checked if this new name is tacken, the first name
        with added number is used as a username
        """
        IMPLEMENT()
        
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

    def clear(self):
        """removes all elements form the mongo db that are users"""
        IMPLEMENT()


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
        # add the other fields
    )
    users.add(gregor)

    print users.find("laszewski@gmail.com")


if __name__ == "__main__":
    main()
