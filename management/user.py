from mongoengine import *
import datetime, time
import hashlib, uuid
#    mongod --noauth --dbpath . --port 27777

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
    

    date_modified = DateTimeField(default=datetime.datetime.now)
    date_created = DateTimeField(default=datetime.datetime.now)
    date_approved = None 
    date_deactivate = None

    def is_active(self):
        # find if user is in active project  
        d2 = datetime.datetime.now #Has an error to correct...
        d3 = self.date_deactivate
        if self.active == True:
            if d3 > d2:
                return True
            else:
            	return False
        else:
            return False
        
    def activate(self):
        self.active = True

    def deactivate(self):
        active = False

    def set_date_deactivate(self): 
    	d_a = datetime.datetime.now() + datetime.timedelta(weeks=24) 
    	self.date_deactivate = d_a  
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

    def objects(self):
        return self.users
    
    def set_username(self, proposal):
        """sets the username to the proposed username. if this name is taken, a

        number is added and checked if this new name is tacken, the first name
        with added number is used as a username
        """
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
        """adds the specified user to mongodb"""
        user.set_date_deactivate()
        if self.verify(user):
            user.save()
        else:
            print "ERROR: a user with the e-mail `{0}` already exists".format(user.email)
            
    def verify(self, user):
        """verifies if the user can be added. Checks if the e-mail is unique. Returns true."""
	_user = User.objects(email=user.email)
        print _user.count() == 0
        return _user.count() == 0

    def find(self, email=None):
        """returns the users based on the give query"""
        if email == None:
            found = User.objects()
            return found
    	else:
            found = User.objects(email=email)
            if found.count() > 0:
                return found[0].to_json()
            else:
                return None

    def clear(self):
        """removes all elements form the mongo db that are users"""
        for user in User.objects:
            user.delete()


def main():

    users = Users()
    users.clear()
    
    gregor = User(
        title = "",
        firstname = "Gregor",
        lastname = "von Laszewski",
        email = "laszewski@gmail.com",
        active = True,
        password = "none",
        phone = "6625768900",
        department = "School of Informatics and Computing",
        institution = "Indiana University",
        address = "Bloomington",
        country = "USA",
        citizenship = "Germany",
        bio = "I work at Indiana University Bloomington"  
                
        
        # add the other fields
    )
    gregor.username = "gregvon"
    gregor.username = users.set_username(gregor.username)
    users.add(gregor)
    
    print    
    print gregor.username
    print gregor.date_created
    print gregor.date_deactivate
    gregor.is_active()
    print


    #print users.find("laszewski@gmail.com")
    
    ifeanyi = User(
        title = "",
        firstname = "Ifeanyi",
        lastname = "Onyenweaku",
        email = "rowlandifeanyi17@gmail.com",
        active = True,
        password = "none",
        phone = "6625768900",
        department = "School of Informatics and Computing",
        institution = "Indiana University",
        address = "Bloomington",
        country = "USA",
        citizenship = "Nigeria",
        bio = "I research at Indiana University Bloomington"  
                
        
        # add the other fields
    )
    ifeanyi.username = "gregvon"
    ifeanyi.username = users.set_username(ifeanyi.username)
    print    
    print ifeanyi.username
    print
    users.add(ifeanyi)

    #print users.find("rowlandifeanyi17@gmail.com")


if __name__ == "__main__":
    main()
