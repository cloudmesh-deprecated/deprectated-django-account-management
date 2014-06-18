How to Write & Display a View using Bootstrapped Theme Django
-----------------------------------------------------------------
In order to write a view in Django do the following::
	
	cd exampleapp
	texteditor views.py
	
In views.py in your app, write your view::
	
	from django.http import HttpResponse
	def index(request):
		return HttpResponse("You got it!")
		
Now go to your individual project and configure your urls.py file::
	
	url(r'^exampleapp/$', 'exampleapp.views.index', name = 'index'),
	
Now do a ``python manage.py syncdb`` and then do a ``python manage.py runserver``
and you should be able to type in ''/SignUp'' behind the local Host address and 
receive the message above. 
