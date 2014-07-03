from mongoengine import *
from mongoengine.context_managers import switch_db
from datetime import datetime
import hashlib, uuid
from user import User, Users


port=27777
db_name = 'project'

def IMPLEMENT():
    print "IMPLEMENT ME"

STATUS = ('pending', 'approved', 'completed', 'denied')

CATEGORY = ('Database', 'FutureGrid', 'other')

DISCIPLINE = ('other')
# see https://ncsesdata.nsf.gov/nsf/srs/webcasp/data/gradstud.htm
# put in discipline.txt and initialize from there through reading the file and codes
#

INSTITUTE_ROLE = ('gaduate student',
                  'undergraduate student',
                  'staff',
                  'faculty',
                  'visitor',
                  'other')
                  
CLUSTERS = ('india',
            'bravo',
            'echo',
            'delta',
            'other', 'None')

SERVICES = ('eucalyptus',
            'openstack',
            'mpi',
            'hadoop',
            'mapreduce',
            'docker',
            'other', 'None')

SOFTWARE = ('other')

PROVISIONING = ('vm',
                'baremetal',
                'container',
                'iaas',
                'paas',
                'other', 'None')

GRANT_ORG = ('NSF',
             'DOE',
             'DoD',
             'NIH',
             'other', 'None')
    
class Project(Document):

    # -------------------------------------------------------------------
    # Project Information
    # -------------------------------------------------------------------
    title  = StringField(required=True)
    abstract    = StringField(required=True) 
    intellectual_merit  = StringField(required=True)
    broader_impact  = StringField(required=True)
    use_of_fg  = StringField(required=True)
    scale_of_use  = StringField(required=True)
    categories =  ListField(StringField(choices=CATEGORY), required=True)
    # example search in a list field
    # Project.objects(categories__contains='education')
    keywords  = ListField(StringField(), required=True)
    primary_discipline =  StringField(choices=DISCIPLINE, required=True)
    orientation  = StringField(required=True)
    contact  = StringField(required=True)
    url = URLField(required=True)
    comment = StringField()
    active = BooleanField(required=True)
    projectid = UUIDField()

    status =  StringField(choices=STATUS,required=True)
    # maybe we do not need active as this may be covered in status
   
    # -------------------------------------------------------------------
    # Member Fields
    # -------------------------------------------------------------------
    lead = StringField( required=True)
    #lead_institutional_role =  StringField(choices=INSTITUTE_ROLE, required=True)
    managers = ListField(StringField())
    #members = ListField(ReferenceField(User), required=True)
    alumnis = ListField(StringField())

    # active_members = lead u managers u members - alumnis
    # if not active : active_members = None

    # -------------------------------------------------------------------
    # Grant Information
    # -------------------------------------------------------------------
    grant_orgnization =  StringField(choices=GRANT_ORG)
    grant_id = StringField()
    grant_url = URLField()


    # -------------------------------------------------------------------
    # Results
    # -------------------------------------------------------------------
    results = StringField()

    # -------------------------------------------------------------------
    # Aggrements
    # -------------------------------------------------------------------
    aggreement_use = BooleanField()
    aggreement_slides = BooleanField()
    aggreement_support = BooleanField()
    aggreement_sotfware = BooleanField()
    aggreement_documentation = BooleanField()

    # -------------------------------------------------------------------
    # Comments
    # -------------------------------------------------------------------
    comments = StringField()

    # -------------------------------------------------------------------
    # Join
    # -------------------------------------------------------------------
    join_open = BooleanField()
    join_notification = BooleanField()

    # -------------------------------------------------------------------
    # Resources
    # -------------------------------------------------------------------
    resources_services = ListField(StringField(choices=SERVICES), required=True)
    resources_software = ListField(StringField(choices=SOFTWARE), required=True)
    resources_clusters = ListField(StringField(choices=CLUSTERS), required=True)
    resources_provision = ListField(StringField(choices=PROVISIONING), required=True)
    
    # BUG how can we add also arbitray info in case of other, mabe ommit choices

    def to_json(self):
        """prints the project as a json object"""
         
        d ={
             "title":self.title,
             "abstract":self.abstract,
             "intellectual_merit":self.intellectual_merit,    
             "broader_impact":self.broader_impact,
             "use_of_fg":self.use_of_fg,
             "scale_of_use":self.scale_of_use,
             "categories":self.categories,
             "keywords":self.keywords,
             "primary_discipline":self.primary_discipline,
             "orientation":self.orientation,
             "contact":self.contact,
             "url":self.url,
             "active":self.active,
             "status":self.status,
             "lead":self.lead,
             #"members":self.members,
             "resources_services":self.resources_services,
             "resources_software":self.resources_software,
             "resources_clusters":self.resources_clusters,
             "resources_provision":self.resources_provision
            }
             
             

    def __str__(self):
        d = self.to_json()
        return str(d)

class Projects(object):

    def __init__(self):
        db = connect(db_name, port=port)
        self.projects = Project.objects()
        #db = connect('user', port=port)
        #self.users = User.objects()
       
        meta = {"db_alias": "Project-db"}
    
    def __str__(self):
        IMPLEMENT()

    def objects(self):
        return self.projects
    
    def add_project(self, project):
    	#_verify = self.verify_user(project.lead, project)
    	#if _verify == True:
    	with switch_db(project, 'User-db') as project:
            print "I am in"
    	    project.save()
    	print project
    	#else:
            #print "ERROR: The user `{0}` has not registered with FutureGrid".format(project.lead)
     
    def verify_user(self, user, project):
    	print "dumb"
        _username = User.objects(username=user.username)
        if _username == True:
            return True
        else:
            return False
            
    def find_by_id(self, id):
        found = Project.objects(projectid=id)
        if found.count() > 0:
            return found[0].to_json()
        else:
            return None
        #User ID or project ID

    def find_by_category(self, category):
    	found = Project.objects(categories=category)
    	print Project.objects(categories=category)
        if found.count() > 0:
            print "yay"
            return found[0].to_json()
        else:
            return None
        

    def find_by_keyword(self, keyword):
        found = Project.objects(keyword=keyword)
        if found.count() > 0:
            return found[0].to_json()
        else:
            return None

    def clear(self):
        """removes all projects from the database"""
        for project in Project.objects:
            project.delete()
    

def main():
    
    #users = Users()
    projects = Projects()
    projects.clear()
    
    #print users.find("rowlandifeanyi17@gmail.com")
    #print "Hereeeeeeeee"
    
    django = Project(
    	    title = "Django Project",
    	    abstract = "This is my abstract",
            intellectual_merit = "All about the merit thingy",    
            broader_impact = "Everything is broad according ...",
            use_of_fg = "Fg is about to use it",
            scale_of_use = "Would be used to implement djandgo",
            categories = ['FutureGrid'],
            keywords = ['sqllite'],
            primary_discipline = "other",  
            orientation = "Lot's of all make",
            contact = "Bloomington",
            url = 'https://www.facebook.com/',
            active = True,
            status = "pending",
            lead = "ifeanyi",
            #members = ['gregor'],
            resources_services = ['hadoop','openstack'],
            resources_software = ['other'],
            resources_clusters = ['india'],
            resources_provision = ['paas']
          )
    print django.abstract
    projects.add_project(django)
    
    print projects.find_by_category('FutureGrid')
             


if __name__ == "__main__":
    main()
             
