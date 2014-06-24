from mongoengine import *
from management1 import User
from management1 import Account

#    mongod --noauth --dbpath . --port 27777

#    ***Would need a list to get its information 
#    ***from as defined on the futuregrid page 

class project(Document):
    information = ReferenceField(project_information)
    requirements = ReferenceField(resource_requirement)
    project_title = StringField()
    category = StringField() 			#***
    keywords = ListField(StringField())
    lead = ReferenceField(Account)
    manager = ReferenceField(Account)
    contact = StringField()
    members = ListField(ReferenceField(Account))
    alumni = ListField(ReferenceField(Account))
    nsf_grant_number = StringField()
    nsf_grant_url = StringField()
    results = StringField()
    nsf_Aggreement = StringField() 		#Yes/No
    slide_collection_aggreement = StringField()	#Yes/No
    other = StringField()
    
class project_information(Document):
    orientation = StringField() 		#***
    primary_discipline = StringField()		#***
    abstract = StringField()
    intellectual_merit = StringField()
    broader_impact = StringField()
    software_contribution = StringField()	#Yes/No
    documentation_contribution = StringField()	#Yes/No
    support_Software = StringField()		#Yes/No
    
    def 
    
class resource_requirement(Document):    
    hardware_resources = ListField(StringField())
    provision_type = ListField(StringField())  
    base_environment = ListField(StringField())
    server = ListField(StringField())
    comment = StringField()
    use_of_fg = StringField()
    scale of use = StringField()
