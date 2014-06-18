from django.conf.urls import patterns, url

from practice1 import models

urlpatterns = patterns('',
	#url (r'^$', views.index, name='index'),
	url (r'^$', models.SignUp, name='signup')
)
