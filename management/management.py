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

    
    def __str__(self):
        return "{0} {1} {3} {4} {5}".format(self.owner,
                                            self.username,
                                            self.email,
                                            self.phone,
                                            self.department,
                                            self.institution,
                                            self.adviser_contact,
                                            self.institute_address,
                                            self.institute_country,
                                            self.url,
                                            self.citizenship,
                                            self.bio,
                                            self.signup_code)

#class Contact(Document):
    







