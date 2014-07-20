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

    url(r'^user/apply/', 'cloudmesh_app.views.user_apply', name = 'user_apply'),
    url(r'^user/approve/', 'cloudmesh_app.views.user_approve', name = 'user_approve'),
    url(r'^user/list/', 'cloudmesh_app.views.user_list', name = 'user_list'),
    url(r'^user/manage/', 'cloudmesh_app.views.user_manage', name = 'user_manage'),                   
    
    url(r'^project/apply/', 'cloudmesh_app.views.project_apply', name = 'project_apply'),
    url(r'^project/approve/', 'cloudmesh_app.views.project_approve', name = 'project_approve'),
    url(r'^project/list/', 'cloudmesh_app.views.project_list', name = 'project_list'),
    url(r'^project/manage/', 'cloudmesh_app.views.project_manage', name = 'project_manage'),
    url(r'^project/results/', 'cloudmesh_app.views.project_result', name = 'project_results'),
    url(r'^project/members/', 'cloudmesh_app.views.project_members', name = 'project_members'),                           
    
)
