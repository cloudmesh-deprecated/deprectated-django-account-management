from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import connect
from cloudmesh_management.user import User, Users
from cloudmesh_management.project import Project, Projects
from cloudmesh_app.forms import ContactForm
from cloudmesh_app.forms import ApplyUserForm, ApplyProjectForm

from django.views.generic.edit import FormView
from django.shortcuts import render

class ApplyProjectView(FormView):
	template_name = 'project_apply_new.html'
	form_class = ApplyProjectForm
	success_url = '/thanks/'
	
	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
            form.do_action()
            return super(ApplyProjectView, self).form_valid(form)

class ApplyUserView(FormView):
    template_name = 'user_apply_new.html'
    form_class = ApplyUserForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.do_action()
        return super(ApplyUserView, self).form_valid(form)


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.do_action()
        return super(ContactView, self).form_valid(form)


def index(request):
    return render(request, 'index.html',)

def list(request):
    return render(request, 'list.html',)

def thanks_msg(request):
    return render(request, 'thanks.html',)

def project_apply(request):
    return render(request, 'project_apply.html',)

#
# USERS
#


def user_apply(request):
    return render(request, 'user_apply.html',)
    
"""
def user_apply(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        user = User(firstname=firstname)
        user.save()
        return render(request, 'thanks.html',)
    
	connect ('user', port=27777)
	users = User.objects()
        return HttpResponse('user_apply.html',
                            {"users":users}, 
                            context_instance=RequestContext(request))
"""

def user_list(request):

    connect ('user', port=27777)
    users = User.objects()
    return render(request, 'user_list.html', {"users": users})

def user_approve(request):
    return render(request, 'user_approve.html',)

def user_manage(request):
    connect ('user', port=27777)
    users = User.objects()
    return render(request, 'user_manage.html', {"users": users})



#
# PROJECTS
#


"""
def project_apply(request):
    return render(request, 'project_apply.html',)
"""
        
def project_list(request):
    connect ('user', port=27777)
    projects = Project.objects()
    print projects
    return render(request, 'project_list.html', {"projects": projects})

def project_approve(request):
    return render(request, 'project_approve.html',)

def project_result(request):
    return render(request, 'project_result.html',)

def project_members(request):
    return render(request, 'project_members.html',)

def project_manage(request):
    connect ('user', port=27777)
    projects = Project.objects()
    print projects
    return render(request, 'project_manage.html', {"projects": projects})

    


