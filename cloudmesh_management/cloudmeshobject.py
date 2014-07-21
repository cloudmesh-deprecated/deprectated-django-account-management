import datetime, time
from mongoengine import Document
from mongoengine import *

class CloudmeshObject(Document):

    active = BooleanField() 
    date_modified = DateTimeField(default=datetime.datetime.now)
    date_created = DateTimeField(default=datetime.datetime.now)
    date_approved = None 
    date_deactivated = DateTimeField()

    meta = {'allow_inheritance': True}

    def fields(self, kind=None):
        if kind is None or kind in ["all"]:
            return [k for k,v in self._fields.iteritems()]
        elif kind in ["optional"]:
            return [k for k,v in self._fields.iteritems() if not v.required]
        elif kind in ["required"]:
            return [k for k,v in self._fields.iteritems() if v.required]    

    def activate(self, state=True): 
    	"""activates a user"""
        self.active = state

    def deactivate(self):
    	"""deactivates a user after the date to deactivate has been reached"""
    	self.activate(state=False)
            
    def set_date_deactivate(self, weeks=24): 
    	"""Sets the date for the user to be deactivated which is after 24 
    	weeks, equivalent to 6 months"""
    	self.date_deactivate = datetime.datetime.now() + datetime.timedelta(weeks=weeks)
        self.activate()
    	return self.date_deactivate

        
