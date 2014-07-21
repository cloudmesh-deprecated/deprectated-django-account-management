# forms.py
from django import forms
from models import Message
from cloudmesh_management.user import User, Users


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def handle_success(self):
    	message = Message.objects.create(
    		name =  self.cleaned_data['name'],
    		message = self.cleaned_data['message']
    	)
    	message.save()
        # send email using the self.cleaned_data dictionary
        print self.cleaned_data
        pass

class ApplyUserView(forms.Form): 
    title = forms.CharField("")
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
    #
    # Affiliation
    #
    institution = forms.CharField()
    department = forms.CharField()
    address = forms.CharField()
    country = forms.CharField()
    adviser_contact = forms.CharField()
    # advisor = pointer to another user
    
    #
    # Message received from either reviewers, 
    # committee or other users. It is a list because 
    # there might be more than one message
    #
    message = forms.CharField(StringField())
   

    def handle_success(self):
    	message = Message.objects.create(
    		name =  self.cleaned_data['name'],
    		message = self.cleaned_data['message']
    	)
    	message.save()
        # send email using the self.cleaned_data dictionary
        print self.cleaned_data
        pass


