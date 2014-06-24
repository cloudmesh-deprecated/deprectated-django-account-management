from mongoengine import *
from management1 import User
from management1 import Account

#    mongod --noauth --dbpath . --port 27777

#    ***Would need a list to get its information 
#    ***from as defined on the futuregrid page 

class project(Document):
    project_title = StringField()
    category = StringField() 			#***
    keywords = ListField(StringField())
    lead = ReferenceField(Account)
    manager = ReferenceField(Account)
    contact = StringField()
    members = ListField(ReferenceField(User))
    alumni = ListField(ReferenceField(User))
    orientation = StringField() 		#***
    primary_discipline = StringField()		#***
    abstract = StringField()
    intellectual_merit = StringField()
    broader_impact = StringField()
    
