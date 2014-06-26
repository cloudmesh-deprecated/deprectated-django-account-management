How to connect Mongodb to Django Bootstrapped theme
==================================================================

* This same information and more can be obtained at 
http://django-mongodb-engine.readthedocs.org/en/latest/index.html *

Make sure you are in virtualenv, if not do the following::
	
	pip install virtualenv
	virtualenv myproject
	source myproject/bin/activate
	
Now install ``Django-nonrel``, ``djangotoolbox``,
& ``Django MongoDB Engine`` to your system::
	
	pip install git+https://github.com/django-nonrel/django@nonrel-1.5
	pip install git+https://github.com/django-nonrel/djangotoolbox
	pip install git+https://github.com/django-nonrel/mongodb-engine
	
Now go into your project's ``settings.py`` file and go to the ``DATABASES ()``
function and add the following::
	
	DATABASES = {
		'default' : {
			'ENGINE' : 'django_mongodb_engine',
			'NAME' : 'my_database'
		}
	}
	
Then run a ``python manage.py syncdb`` and a ``python manage.py runserver`` and 
then you should be connected. 

*If you want the bootstrapped theme, do a ``pip install django-admin-bootstrapped``
and add `` 'django_admin_bootstrapped', `` before the ``django.contrib.admin``
app in the ``INSTALLED _APPS`` list.
