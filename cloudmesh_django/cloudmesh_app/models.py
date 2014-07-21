from django.db import models
from mongoengine import *
#from user import User, Users
#from project import Project, Project

# Create your models here.

class Message(Document):
        name = StringField(max_length=50)
        message = StringField(max_length=500)

