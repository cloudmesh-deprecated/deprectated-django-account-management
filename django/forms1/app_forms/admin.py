from django.contrib import admin
from django.shortcuts import redirect
from admin_views.admin import AdminViews 
from .models import TestModel

# Register your models here.

#class PostFormAdmin(admin.
#admin.site.register(PostForm)

class TestAdmin(AdminViews):
    admin_views = (
        ('Add content to Form', 'post_form_upload'),
    )
    
    def process(self, *args, **kwargs):
        return redirect('http://127.0.0.1:8000/admin')

admin.site.register(TestModel, TestAdmin)
