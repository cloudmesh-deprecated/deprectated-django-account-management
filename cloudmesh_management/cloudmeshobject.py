import datetime, time
from mongoengine import Document
from mongoengine import *

from mongoengine import fields


def update_document(document, data_dict):

    def field_value(field, value):

        if field.__class__ in (fields.ListField, fields.SortedListField):
            return [
                field_value(field.field, item)
                for item in value
            ]
        if field.__class__ in (
            fields.EmbeddedDocumentField,
            fields.GenericEmbeddedDocumentField,
            fields.ReferenceField,
            fields.GenericReferenceField
        ):
            return field.document_type(**value)
        else:
            return value

    [setattr(
        document, key,
        field_value(document._fields[key], value)
    ) for key, value in data_dict.items()]

    return document

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

        
