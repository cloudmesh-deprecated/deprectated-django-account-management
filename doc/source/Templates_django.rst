Using Templates in Views in Django
--------------------------------------------------

Go into your projects ``settings.py`` file and add these Directories
(unless you already have them in the file)::
	
	TEMPLATE_LOADERS = (
		'django.template.loaders.filesystem.Loader',
		'django.template.loaders.app_directories.Loader',
	)
	
	.........
	
	TEMPLATE_DIRS = (
		'/home/django/yoursite/templates',
	)

Now go into your project folder create a template directory (``mkdir templates``)
and in this directory create the html skeleton for your view. 
For example::
	
	<html><body>It is now {{ current_date }}.</body></html> 
	
Now go back to your view and create your view or if you need to add your imports
For example::
	
	from django.template.loader import get_template
	from django.template import Context
	from django.shortcuts import render
	from django.http import HttpResponse
	import datetime
	
	def current_datetime(request):
		now = datetime.datetime.now()
		t = get_template('name of your template file.html')
		html = t.render(Context({ 'current_date':now}))
		return HttpResponse(html) 
		
You should get a display with It is now (and the current time here) when you login
to the server. The website `Link text http://www.djangobook.com/en/2.0/chapter04.html` 
is a great resource to look at to understand the syntax of the above code 

