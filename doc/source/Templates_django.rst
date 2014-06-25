Loading a Template in Django
===========================================

Create an app ``python manage.py startapp exampleapp_name``

Then, In project do the following::
	
	mkdir templates 
	mkdir static
	cd static
	mkdir js
	mkdir css
	cd exampleproject
	texteditor settings.py
	
In the ``settings.py`` file go to ``TEMPLATE_DIRS ()``, ``TEMPLATE_LOADERS ()``,
& ``STATICFILES_DIRS ()`` functions and write the path to the templates 
folder you just created and add these parameters to ``TEMPLATE_LOADERS ()`` &
``STATICFILES_DIRS ()``::
	
	TEMPLATE_LOADERS = (
		'django.template.loaders.filesystem.Loader',
		'django.template.loaders.app_directories.Loader',
	)
	.........
	TEMPLATE_DIRS = (
		'/home/django/examplesite/templates',
	)
	
	STATICFILES_DIRS = (
		'/home/django/examplesite/static',
	)
	
Now go to your newly created Template directory and create a file named ``base.html``.
In this file, copy and paste the html from your desired template from the 
``http://getbootstrap.com`` website or your own created html

1) View the source code of your chosen template and click on the link below
``<! -- Bootstrap core.css -->`` & ``<!-- Custom styles for this template -->``

2) After clicking on both of these links - right-click on the page of the code 
and choose ``save as`` and save files to css folder in static directory 

..
	Repeat Steps 1 & 2 with the link at the bottom of the source code (Below
	``<!-- Placed at the end of the document so the pages load faster -->``)
	and save in js folder in static directory 
	
Now go back to the ``base.html`` file and create the section ``{% block content %}``
& ``{% endblock %}`` (for syntax go to www.djangobook.com/en/2.0/chapter04.html)

In the templates directory, create another html file and in the file do the 
following::
	
	{% extends "base.html" %}
	
	{% block content %} The template works! {% endblock %}
	
Now go into your app and create your view::
	
	from django.shortcuts import render 
	 
	def index(request):  
		return render(request, 'your_html_file.html',)
		
Now go into your templates directory and go to your ``base.html`` file and add
the paths to your created files in the static folder for both css and js. For example::
	
	<link href = "/static/css/boostrap.min.css" rel="stylesheet">
	<link href = "/static/css/specified_template_used.css" rel="stylesheet">
	
	<script src="/static/js/jquery.min.js"></script>
	<script src="/static/js/bootstrap.min.js"></script>
		
Now go into your project's ``urls.py`` file and do the following::
	
	url(r'^index/', 'exampleapp_name.views.index', name = 'index')
	
Then finally do a ``python manage.py collectstatic`` and type yes to the prompt
and then run ``python manage.py runserver``. 
	


