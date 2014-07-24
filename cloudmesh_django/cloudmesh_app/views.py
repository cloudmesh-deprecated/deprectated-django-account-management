from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import connect
from cloudmesh_management.user import User as MongoUser 
from cloudmesh_management.user import Users
from cloudmesh_management.project import Project, Projects
from cloudmesh_management.project import STATUS as ProjectSTATUS
from cloudmesh_management.user import STATUS as UserSTATUS
from cloudmesh_app.forms import ContactForm
from cloudmesh_app.forms import ApplyUserForm, ApplyProjectForm, EditUserForm

from pprint import pprint
import os


class ApplyProjectView(FormView):
	template_name = 'project_apply.html'
	form_class = ApplyProjectForm
	success_url = '/thanks/'
	
	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
            form.do_action()
            return super(ApplyProjectView, self).form_valid(form)

class ApplyUserView(FormView):
    template_name = 'user_apply.html'
    form_class = ApplyUserForm
    success_url = '/thanks/'

    title = "hallo"
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.do_action()
        return super(ApplyUserView, self).form_valid(form)


    """
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print ">>>>>POSTING", request.POST
            return HttpResponseRedirect('/thanks/')

        return render(request, self.template_name, {'form': form})
    """
    
class EditUserView(FormView):
    template_name = 'user_apply.html'
    form_class = EditUserForm
    success_url = '/thanks/' 


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
    
def user_list(request):

    connect ('user', port=27777)
    users = MongoUser.objects()
    return render(request, 'user_list.html', {"users": users})

def user_approve(request):
    return render(request, 'user_approve.html',)

def user_manage(request):

    if request.method == 'POST':
        if 'selectedusers' in request.POST:
            print ">>> POSTING", request.POST
            data = dict(request.POST.iterlists())
            print "DATA", data
            action = str(data['button'][0])
            print "ACTION", action            
            usernames = data['selectedusers']
            
            #pprint(request.__dict__)
            msg = str(request.POST)

            for username in usernames:
                user = MongoUser.objects(username=username)[0]
                user.status = action                
                user.save()

            
    connect ('user', port=27777)
    users = MongoUser.objects()
    return render(request, 'user_manage.html', {"users": users, 'states': UserSTATUS})

def user_profile(request):
    username = os.path.basename(request.path)        
    connect ('user', port=27777)
    try:
        user = MongoUser.objects(username=username)
        print user
        print user.count()
        if user.count() == 1:
            print user[0]
            print user[0].username            
            return render(request, 'user_profile.html', {"user": user[0]})
        else:
            raise Exception
    except:
        print "Error: Username not found"
        return render(request, 'error.html', {"error": "The user does not exist"}) 


def user_edit(request):
    username = os.path.basename(request.path)        
    connect ('user', port=27777)

    try:
        user = MongoUser.objects(username=username)
    except:
        print "Error: Username not found"
        return render(request, 'error.html', {"error": "The user does not exist"}) 

    
    if request.method == 'GET':
        
        return render(request, 'user_edit.html', {"user": user[0], "states": ['save', 'cancel']})                

    elif request.method == 'POST':

        data = dict(request.POST.iterlists())
        action = str(data['button'][0])
        del data['button']
        for key in data:
            data[key] = data[key][0]

        user = MongoUser.objects(username=username)[0]
        if action == 'save':

            user.bio = data["bio"]
            user.citizenship = data["citizenship"]
            user.firstname = data["firstname"]
            user.title = data["title"]
            user.url = data["url"]
            user.lastname = data["lastname"]
            user.address = data["address"]
            user.institution = data["institution"]
            user.phone = data["phone"]
            user.advisor = data["advisor"]
            user.department = data["department"]
            user.csrfmiddlewaretoken = data["csrfmiddlewaretoken"]
            user.country = data["country"]
            user.email = data["email"]

            user.save()

        return render(request, 'user_edit.html', {"user": user, "states": ['save', 'cancel']})                
        
#

# PROJECTS
#


def project_edit(request):
    projectid = os.path.basename(request.path)        
    connect ('user', port=27777)

    try:
        project = Project.objects(projectid=projectid)
    except:
        print "Error: Username not found"
        return render(request, 'error.html', {"error": "The user does not exist"}) 

    
    if request.method == 'GET':
        print "GETTING"
        
        return render(request, 'project_edit.html', {"project": project[0], "states": ['save', 'cancel']})                

    elif request.method == 'POST':

        print "POSTING"
        data = dict(request.POST.iterlists())
        action = str(data['button'][0])
        #del data['button']
        for key in data:
            data[key] = data[key][0]
    
        print ">>>>ACTION", action
        #project = Project.objects(projectid=projectid)[0]
        project = project[0]        
            
        if action == 'save':
            for d in data:
                print d, ":", data[d]
            try:
                project.title = data["title"]
                project.abstract = data["abstract"]
                project.intellectual_merit = data["intellectual_merit"]
                project.broader_impact = data["broader_impact"]
                project.use_of_fg = data["use_of_fg"]
                project.scale_of_use = data["scale_of_use"]
                """

                #
                # things that should not be changed
                #
                #project.active = data["active"]
                #project.status = data["status"]
                #project.projectid = data["projectid"]

                #
                # after apoproval this should not be changed either
                #
                project.aggreement_use = data["aggreement_use"]
                project.aggreement_slides = data["aggreement_slides"]
                project.aggreement_support = data["aggreement_support"]
                project.aggreement_sotfware = data["aggreement_sotfware"]
                project.aggreement_documentation = data["aggreement_documentation"]
                                                                
                project.categories = data["categories"]
                project.keywords = data["keywords"]
                project.primary_discipline = data["primary_discipline"]
                project.orientation = data["orientation"]
                project.contact = data["contact"]
                project.url = data["url"]
                project.comment = data["comment"]


                project.lead = data["lead"]
                project.managers = data["managers"]
                project.members = data["members"]
                project.alumnis = data["alumnis"]
                project.grant_orgnization = data["grant_orgnization"]
                project.grant_id = data["grant_id"]
                project.grant_url = data["grant_url"]
                project.results = data["results"]
                project.comments = data["comments"]
                project.join_open = data["join_open"]
                project.join_notification = data["join_notification"]
                project.resources_services = data["resources_services"]
                project.resources_software = data["resources_software"]
                project.resources_clusters = data["resources_clusters"]
                project.resources_provision = data["resources_provision"]
                """
                project.save()                
                print "SAVING"
                
            except Exception, e:
                print "ERROR",e 
                


        return render(request, 'project_edit.html', {"project": project, "states": ['save', 'cancel']})                
        

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

    if request.method == 'POST':
        #
        # check for selection
        #
        if 'selectedprojects' in request.POST:
            data = dict(request.POST.iterlists())
            print data
            project_ids = data['selectedprojects']
            action = str(data['button'][0])
            print "ACTION", action, action in ProjectSTATUS, 'approved' in ProjectSTATUS
            print "PROJECTS", project_ids
            
            for projectid in project_ids:
                project = Project.objects(projectid=projectid)[0]
                project.status = action                
                project.save()

    connect ('user', port=27777)
    projects = Project.objects()
    print projects
    return render(request, 'project_manage.html', {"projects": projects, 'states': ProjectSTATUS})

def project_profile(request):
    projectid = os.path.basename(request.path)
    print projectid 
    connect ('user', port=27777)
    try:
        project = Project.objects(projectid=projectid)
        if project.count() == 1:
            return render(request, 'project_profile.html', {"project": project[0]})
        else:
            raise Exception
    except:
        print "Error: Project not found"
        return render(request, 'error.html', {"error": "The project does not exist"}) 



    


