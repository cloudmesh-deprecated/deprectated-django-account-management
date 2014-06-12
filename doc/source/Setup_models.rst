Setup Models using Bootstrapped Theme Django
======================================================

First, cd into your project in the terminal and type the following::
	
	$ python manage.py startapp exampleapp
	$ cd exampleapp
	$ texteditor models.py
	
Here's an example of a modified models.py file in exampleapp::
	
	from django.db import models
	from django.utils.encoding import smart_unicode

	# Create your models here.

	class SignUp(models.Model):
	first_name = models.CharField(max_length=120, 
				      null =True, 
                                      blank=True)
	last_name = models.CharField(max_length=120, 
                                     null =True, 
                                     blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	def __unicode__(self):
		return smart_unicode(self.email)
		
After modifying go to ``$ texteditor admin.py`` and modify the file. 
Here's an example::
	
	from django.contrib import admin

	# Register your models here.
	from .models import SignUp

	class SignUpAdmin(admin.ModelAdmin):
		class Meta:
			model =SignUp
		
	admin.site.register(SignUp, SignUpAdmin)
	
Now go into your django project and do the following::
	
	$ texteditor settings.py 
	.. Add newly created app to INSTALLED_APPS
	INSTALLED_APPS = (
	'django_admin_bootstrapped',
	.....
	.....
	'exampleapp',
	)
	
Below the ``STATIC_URL = '/static/'`` add the following::
	
	#Template location
	TEMPLATE_DIRS = (
		os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
	
	)
	
Now in your do a ``pip install django-admin-bootstrapped`` in the terminal and 
then a ``python manage.py syncdb`` and ``python manage.py runserver`` and you 
should see your django-bootstrapped theme with model working!
