from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudmesh_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/', 'cloudmesh_app.views.index', name = 'index'),
    url(r'^$', 'cloudmesh_app.views.index', name = 'index'),

    url(r'^list/', 'cloudmesh_app.views.list', name = 'list'),       
    
)
