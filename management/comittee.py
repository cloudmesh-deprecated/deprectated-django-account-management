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

STATUS = ('pending', 'approved', 'completed', 'denied')
    
class Committee(Document):
    # status = StringField(choices=STATUS)
    committee = StringField(Committee)
    project = ReferenceField(Project)
    reviewers = ListField(ReferenceField(User))
    default_reviewer = ListField(ReferenceField(User))
    reviews = StringField()
    
    def __str__(self):
        return "{0} {1} {2} {3}".format(self.project,self.default_reviewer)

    def get_default_reviewer(self, user_name):
    	default_reviewer = users.find_user(user_name)
    	self.reviewers.append(default_reviewer)
    	return self.project.reviewers

    def set_review(self, project, user, msg):
    	"""by set_review, do you mean to state whether
    	approved or not and what type of message am I meant to 
    	pass into this function"""
    	
        IMPLEMENT()

    def add_reviewer(self, project, user):
    	self.project.reviewers.append(user)
        IMPLEMENT()

    def delete_reviewer(self, project, user):
    	self.project.reviewers.delete(user)
        IMPLEMENT()

    def add_default_reviewer(self, user):
    	self.project.reviewers.append(user)
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

    users = Users()
    projects = Projects()
    committee = Committee()
    
    _user = users.find_user("gregvon12")
    committee.project = projects.find_by_title("Django Project")
    #print _user, ": \n\n", _project
    
    django_committee = Committee(project = projects.find_by_title("Django Project"),
    	    			 reviewer = users.find_user("gregvon12"),
    	    
    
    committee.add_reviewer(committee.project, _user)
    #print committee.reviewers

    
    
    
    
    
    


if __name__ == "__main__":
    main()               
