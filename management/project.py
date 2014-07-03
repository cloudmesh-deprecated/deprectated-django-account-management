from mongoengine import *
from datetime import datetime
import hashlib, uuid
from management import User, Users


port=27777
db_name = 'project'

def IMPLEMENT():
    print "IMPLEMENT ME"

STATUS = ('pending', 'approved', 'completed', 'denied')

CATEGORY = ('other')

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
    title  = StringFiled(required=True)
    abstract    = StringFiled(required=True) 
    intellectual_merit  = StringFiled(required=True)
    broader_impact  = StringFiled(required=True)
    use_of_fg  = StringFiled(required=True)
    scale_of_use  = StringFiled(required=True)
    categories =  ListField(StringField(choices=CATEGORY), required=True)
    # example search in a list field
    # Project.objects(categories__contains='education')
    keywords  = ListField(StringFiled(), required=True)
    primary_discipline =  StringField(choices=DISCIPLINE, required=True)
    orientation  = StringFiled(required=True)
    contact  = StringFiled(required=True)
    url = URLField(required=True)
    comment = StringFiled()
    active = BooleanField(required=True)
    projectid = UUIDField()

    status =  StringField(choices=STATUS,required=True)
    # maybe we do not need active as this may be covered in status
   
    # -------------------------------------------------------------------
    # Member Fields
    # -------------------------------------------------------------------
    lead = ReferenceField(User, required=True)
    lead_institutional_role =  StringField(choices=INSTITUTE_ROLE, required=True)
    managers = ListField(ReferenceField(User))
    members = ListField(ReferenceField(User), required=True)
    alumnis = ListField(ReferenceField(User))

    # active_members = lead u managers u members - alumnis
    # if not active : active_members = None

    # -------------------------------------------------------------------
    # Grant Information
    # -------------------------------------------------------------------
    grant_orgnization =  StringField(choices=GRANT_ORG)
    grant_id = StringFiled()
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
    resources_provision == ListField(StringField(choices=PROVISIONING), required=True)

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
             "members":self.members,
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
        self.db = connect(db_name, port=port)
        self.projects = Project.objects()
        db = connect('user', port=port)
        self.users = User.objects()
    
    def __str__(self):
        IMPLEMENT()

    def objects(self)
        return self.projects
     
    def verify_user(self, user)
        _username = User.objects(username=user.username)
        if _username == True:
            return True
        else:
            return "This user has not registered"
            
    def find_by_id(self, id):
        found = User.objects(projectid=id)
        if found.count() > 0:
            return found[0].to_json()
        else:
            return None
        #User ID or project ID

    def find_by_category(self, category):
    	found = User.objects(categories=category)
        if found.count() > 0:
            return found[0].to_json()
        else:
            return None
        IMPLEMENT()

    def find_by_keyword(self, keyword):
        IMPLEMENT()

    def clear(self):
        """removes all projects from the database"""
        for project in Project.objects:
            project.delete()
        