from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('InfoProjects.views',
    # Examples:
    # url(r'^$', 'projects2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('InfoProjects.urls')),
    url(r'^InfoProjects/$', 'InfoProject_list'),
    url(r'^InfoProjects/(?P<pk>[0-9]+)/$', 'InfoProject_detail'),	
    url(r'^index/', 'InfoProjects.views.index', name = 'index'),
)
