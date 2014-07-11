from mongoengine import *
from datetime import datetime
from project import Project, Projects
from user import User, Users

port=27777
db_name = 'project'

users = Users()
projects = Projects()

def IMPLEMENT():
    print "IMPLEMENT ME"

DEFAULT_REVIEWERS = ('gregvon', 'jeff', 'gregvon1')

STATUS = ('pending', 'approved', 'disapproved')

CHOICES = ('Yes', 'No')
    
class Committee(Document):
    # status = StringField(choices=STATUS)
    projects = ListField(StringField())
    reviewers = ListField(ReferenceField(User))
    default_reviewer = ListField(ReferenceField(User))
    reviews = StringField()
    #--------------------------------------------------------------------
    #	Default value showing if this is the first time the project is being applied for or not
    #--------------------------------------------------------------------
    default = StringField(choices=CHOICES, default = 'Yes')
    
    
    def __str__(self):
        return "{0} {1} {2} {3}".format(self.status,self.reviewers)
        
    def get_project(self, title):
        """This function wold be deleted later after we have been able
        call this class from the project class, hence this is a sample"""
        _project = projects.find_by_title("Django")

    def get_reviewer(self, user_name):
    	if default == 'Yes':
    	    count = len(STATUS)
    	    while count <= 0:
    	        default_reviewer = users.find_user(STATUS[count])
    	        add_default_reviewer(default_reviewer)
    	    default == 'No'
    	else if default == 'No':
    	    _reviewer = users.find_user(STATUS[count])
    	    add_reviewer#****I am here****
    
    def add_default_reviewer(self, user):
    	self.reviewers.append(user)

    def add_reviewer(self, project, user):
    	self.reviewers.append(user)
        IMPLEMENT()

    def set_review(self, project, user, msg):
    	"""by set_review, do you mean to state whether
    	approved or not and what type of message am I meant to 
    	pass into this function"""
    	
        IMPLEMENT()

    def delete_reviewer(self, project, user):
    	#self.project.reviewers.delete(user)***wrong***
        IMPLEMENT()

    def delete_default_reviewer(self, user):
        IMPLEMENT()

    def notify_project_management(self, project, msg):
        IMPLEMENT()
                
    def notify_project_members(self, project, msg):
        IMPLEMENT()

    def notify_project_alumni(self, project, msg):
        IMPLEMENT()

    def notify_reviewers(self, project, msg):
        IMPLEMENT()

    def notify_all_reviewers(self, msg):
        IMPLEMENT()

    def enable(self, bool):
        """enables or disables reviews, useful for maintenance"""
        IMPLEMENT()

    def pending_projects(self):
        return self.get_by_status("pending")

    def approved_projects(self):
        return self.get_by_status("approved")        

    def disproved_projects(self):
        return self.get_by_status("disproved")                

    def completed_projects(self):
        return self.get_by_status("completed")                        

    def get_by_status(self,  status):
        if status in STATUS:
            IMPLEMENT()
        else:
            print "ERROR: wrong status", status
            return None


def main():

    comittee = Committe()
    
    
	
	
if __name__ == "__main__":
    main()
    
    
    
    
    
    
