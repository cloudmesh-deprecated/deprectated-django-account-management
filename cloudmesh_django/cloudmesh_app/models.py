from django.db import models
from mongoengine import *
from user import User, Users
from project import Project, Project

# Create your models here.

port=27777

def IMPLEMENT():
    print "IMPLEMENT ME"
'''
def generate_password_hash(password)
    # maybe using passlib https://pypi.python.org/pypi/passlib
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    return hashed_password'''
    
class User(Document):
    """This class is sued to represent a user"""

    #
    # User Information
    #
    username = StringField(required=True)
    
    title = StringField("")
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    address = StringField(required=True)
    Password = StringField(required=True)
    
     def is_active(self):
        """finds if a user is active or not"""
        d1 = datetime.datetime.now()
        if self.active == True:
            if d1 > self.date_deactivate:
                return True
            else:
            	return False
        else:
            return False
        
    def activate(self): 
    	"""activates a user"""
        self.active = True

    def deactivate(self):
    	"""deactivates a user after the date to deactivate has been reached"""
        check = is_active(self)
        if check == False:
            force_deactivate()
            
    def force_deactivate(self):
    	"""forces a user to deactivate without checking if the date to be 
    	deactivated has been reached or not"""
    	active = False

    def set_date_deactivate(self): 
    	"""Sets the date for the user to be deactivated which is after 24 
    	weeks, equivalent to 6 months"""
    	self.date_deactivate = datetime.datetime.now() + datetime.timedelta(weeks=24) 
    	return self.date_deactivate

    def set_password(self, password):
        #self.password_hash = generate_password_hash(password)
        pass
        
    def check_password(self, password):
        #return check_password_hash(self.password_hash, password)
        pass
        
    def to_json(self):
        """prints the user as a json object"""
        
        d ={
            "title" : self.title,
            "firstname" : self.firstname,
            "lastname" :  self.lastname,
            "email" : self.email,
            "active" : self.active,
            #"password" : self.password,
            "userid" : self.userid,
            "date_modified" : self.date_modified,
            
            "phone":self.phone,
            "department":self.department,
            "institution":self.institution,
            
            "address":self.address,
            "country":self.country,
           
            "citizenship":self.citizenship,
            "bio":self.bio,
            "username":self.username,
            #"adviser_contact":self.adviser_contact,
             #"url":self.url,
            #"signup_code":self.signup_code}

        }
         
        try:
            d['url']=self.url
            d['adviser_contact']=self.adviser_contact
        except:
            pass
        return d
    
    def __str__(self):
        return "{0} {1} {2} {3}".format(self.title,self.firstname, self.lastname, self.email)

class Users(object):

    def __init__(self):
        db = connect('user', port=port)
        self.users = User.objects()
        
        meta = {"db_alias": "default"}

    def objects(self):
        return self.users
    
    def set_username(self, proposal):
        """sets the username to the proposed username. if this name is taken, a
        number is added and checked if this new name is tacken, the first name
        with added number is used as a username
        """
        proposal = proposal.lower()
        num = 1
        same = True
        while (same == True):
            _username = User.objects(username=proposal)
            if _username.count() > 0:
                proposal = proposal + str(num)
                num = num + 1
            else:
                return proposal
                
    def add(self, user):
        """adds the specified user to mongodb, as well as activates the users' account
        as well as set's the deactivation date"""
        user.username = self.set_username(user.username)
        user.set_date_deactivate()
        user.is_active()
        if self.verify(user):
            #print user.to_json()
            user.save()
        else:
            print "ERROR: a user with the e-mail `{0}` already exists".format(user.email)
            
    def verify(self, user):
        """verifies if the user can be added. Checks if the e-mail is unique. Returns true."""
	_user = User.objects(email=user.email)
        return _user.count() == 0

    def find(self, email=None):
        """returns the users based on the given query"""
        print "Users"
        if email == None:
            for user in User.objects:
                print 80 * "="
                pprint (user.to_json())
            print 80 * "="                
    	else:
            found = User.objects(email=email)
            if found.count() > 0:
                return found[0].to_json()
            else:
                return None
            
    def find_user(self, username):
    	"""returns a user based on the username"""
    	for user in User.objects:
    	    if user.username == username:
    	        return user
    	    	break
    	    	
    def clear(self):
        """removes all elements form the mongo db that are users"""
        for user in User.objects:
            user.delete()


