# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def handle_success(self):
        # send email using the self.cleaned_data dictionary
        print self.cleaned_data
        pass