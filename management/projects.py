from mongoengine import *
from management1 import User
from management1 import Account

#    mongod --noauth --dbpath . --port 27777

#    ***Would need a list to get its information 
#    ***from as defined on the futuregrid page 

    
class project_information(Document):
    orientation = StringField() 		#***
    primary_discipline = StringField()		#***
    abstract = StringField()
    intellectual_merit = StringField()
    broader_impact = StringField()
    software_contribution = StringField()	#Yes/No
    documentation_contribution = StringField()	#Yes/No
    support_Software = StringField()		#Yes/No
    
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self.orientation, self.primary_discipline,
        						self.abstract, self.intellectual_merit,
        						self.broader_impact, self.software_contribution,
        						self.documentation_contribution, self.support_Software)
    
class resource_requirement(Document):    
    hardware_resources = ListField(StringField())
    provision_type = ListField(StringField())  
    base_environment = ListField(StringField())
    server = ListField(StringField())
    comment = StringField()
    use_of_fg = StringField()
    scale_of_use = StringField()
    
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}".format(self.hardware_resources, self.provision_type,
        					    self.base_environment, self.server,
        					    self.comment, self.use_of_fg,
        					    self.scale_of_use)

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
    
    def to_json(self):
        u = {"information":self.information, 
             "requirements":self.requirements,
             "project_title":self.project_title, 
             "category":self.category, 
             "keywords":self.keywords, 
             "lead":self.lead, 
             "manager":self.manager, 
             "contact":self.contact,
             "members":self.members, 
             "alumni":self.alumni,
             "nsf_grant_number":self.nsf_grant_number, 
             "nsf_grant_url":self.nsf_grant_url, 
             "results":self.results,
             "nsf_Aggreement":self.nsf_Aggreement, 
             "slide_collection_aggreement":self.slide_collection_aggreement,
             "other":self.other}
             
    def __str__(self):
        u = self.to_json()
        return str(u)
