# forms.py
from django import forms
from models import Message
from cloudmesh_management.user import User, Users
from mongoengine import connect
from cloudmesh_management.cloudmeshobject import update_document
from cloudmesh_management.generate import random_user
from cloudmesh_management.project import Project, Projects

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def do_action(self):
    	message = Message.objects.create(
    		name =  self.cleaned_data['name'],
    		message = self.cleaned_data['message']
    	)
    	message.save()
        # send email using the self.cleaned_data dictionary
        print self.cleaned_data
        pass


class ApplyUserForm(forms.Form): 
    username = forms.CharField()    
    title = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.CharField()
    url = forms.CharField()
    citizenship = forms.CharField()
    bio = forms.CharField()
    password = forms.CharField()
    userid = forms.CharField()
    phone = forms.CharField()
    projects = forms.CharField() 
    institution = forms.CharField()
    department = forms.CharField()
    address = forms.CharField()
    country = forms.CharField()
    adviser_contact = forms.CharField()

    def do_action(self):
        print "CLEANED", self.cleaned_data
        try:
            connect ('user', port=27777)
            users = Users()
        except:
            print "ERROR: INternal Server error, please contact the admin"
            pass

        try:
            user = User (
                title = self.cleaned_data["title"],
                firstname = self.cleaned_data["firstname"],
                lastname = self.cleaned_data["lastname"],
                email = self.cleaned_data["email"], 
                username = self.cleaned_data["username"], 
                password = self.cleaned_data["password"],
                phone = self.cleaned_data["phone"], 
                department = self.cleaned_data["department"], 
                institution = self.cleaned_data["institution"],
                address = self.cleaned_data["address"],
                country = self.cleaned_data["country"],
                citizenship = self.cleaned_data["citizenship"],
                bio = self.cleaned_data["bio"],
            )
            users.add(user)
            pass
        except Exception, e:
            print e
            pass
    
    
    
class ApplyProjectForm(forms.Form):    
    title = forms.CharField()
    abstract = forms.CharField()
    broader_impact = forms.CharField()
    intellectual_merit = forms.CharField()
    scale_of_use = forms.CharField()
    use_of_fg = forms.CharField()
    categories = forms.CharField()
    keywords = forms.CharField()

    def do_action(self):
        print "CLEANED", self.cleaned_data
        try:
            connect ('user', port=27777)
            users = Users()
        except:
            print "ERROR: INternal Server error, please contact the admin"
            pass

        try:
            project = Project (
                title = self.cleaned_data["title"],
                abstract = self.cleaned_data["abstract"],
                broader_impact = self.cleaned_data["broader_impact"],
                intellectual_merit = self.cleaned_data["intellectual_merit"], 
                scale_of_use = self.cleaned_data["scale_of_use"], 
                use_of_fg = self.cleaned_data["use_of_fg"],
                categories = self.cleaned_data["categories"], 
                keywords = self.cleaned_data["keywords"], 
                
            )
            projects.add(project)
            pass
        except Exception, e:
            print e
            pass


