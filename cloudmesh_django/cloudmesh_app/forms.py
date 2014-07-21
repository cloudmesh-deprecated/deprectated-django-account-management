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

