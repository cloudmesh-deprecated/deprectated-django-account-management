from mongoengine import *
from datetime import datetime

port=27777
db_name = 'project'

def IMPLEMENT():
    print "IMPLEMENT ME"

STATUS = ('pending', 'approved', 'completed', 'denied')
    
class Committee(Document):

    # status = StringField(choices=STATUS)
    project = ReferenceField(project)
    
    def __str__(self):
        IMPLEMENT()

    def set_review(self, project, user, msg):
        IMPLEMENT()

    def add_reviewer(self, project, user):
        IMPLEMENT()

    def delete_reviewer(self, project, user):
        IMPLEMENT()

    def add_default_reviewer(self, user):
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

    def enable(self, bool)
        """enables or disables reviews, useful for maintenance"""
        IMPLEMENT()

    def pending_projects(self)
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
            
                
