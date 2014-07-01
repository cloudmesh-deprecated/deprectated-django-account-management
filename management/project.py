from mongoengine import *
from datetime import datetime

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
            'other')

SERVICES = ('eucalyptus',
            'openstack',
            'mpi',
            'hadoop',
            'map/reduce',
            'docker',
            'other')

SOFTWARE = ('other')

PROVISIONING = ('vm',
                'baremetal',
                'container',
                'iaas',
                'paas',
                'other')

GRANT_ORG = ('NSF',
             'DOE',
             'DoD',
             'NIH',
             'other')
    
class Project(Document):

    # -------------------------------------------------------------------
    # Project Information
    # -------------------------------------------------------------------
    title  = StringFiled()
    abstract    = StringFiled()
    intellectual_merit  = StringFiled()
    broader_impact  = StringFiled()
    use_of_fg  = StringFiled()
    scale_of_use  = StringFiled()
    categories =  ListField(StringField(choices=CATEGORY))
    # example search in a list field
    # Project.objects(categories__contains='education')
    keywords  = ListField(StringFiled())
    primary_discipline =  StringField(choices=DISCIPLINE)
    orientation  = StringFiled()
    contact  = StringFiled()
    url = URLField()
    comment = StringFiled()
    active = BooleanField()

    status =  StringField(choices=STATUS)
    # maybe we do not need active as this may be covered in status
   
    # -------------------------------------------------------------------
    # Member Fields
    # -------------------------------------------------------------------
    lead = ReferenceField(User)
    lead_institutional_role =  StringField(choices=INSTITUTE_ROLE)
    managers = ListField(ReferenceField(User))
    members = ListField(ReferenceField(User))
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
    resources_services = ListField(StringField(choices=SERVICES))
    resources_software = ListField(StringField(choices=SOFTWARE))
    resources_clusters = ListField(StringField(choices=CLUSTERS))
    resources_provision == ListField(StringField(choices=PROVISIONING))

    # BUG how can we add also arbitray info in case of other, mabe ommit choices


     def __str__(self):
         IMPLEMENT()

class Projects(object):

    def __init__(self):
        self.db = connect(db_name, port=port)
        self.projects = Project.objects()
    
    def __str__(self):
        IMPLEMENT()

    def objects(self)
        return self.projects
            
    def find_by_id(self, id):
        IMPLEMENT()

    def find_by_category(self, category):
        IMPLEMENT()

    def find_by_keyword(self, keyword):
        IMPLEMENT()

    def clear(self):
        IMPLEMENT()
        
