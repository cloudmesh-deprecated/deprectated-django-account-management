from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    
    url(r'^practice1/', include ('practice1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
