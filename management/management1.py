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
    






