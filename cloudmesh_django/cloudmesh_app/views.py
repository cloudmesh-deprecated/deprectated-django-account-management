from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def list(request):
    return render(request, 'list.html',)

def project_apply(request):
    return render(request, 'project_apply.html',)

#
# USERS
#

def user_apply(request):
    return render(request, 'user_apply.html',)

def user_list(request):
    return render(request, 'user_list.html',)

def user_approve(request):
    return render(request, 'user_approve.html',)

def user_manage(request):
    return render(request, 'user_manage.html',)

#
# PROJECTS
#

def project_apply(request):
    return render(request, 'project_apply.html',)

def project_list(request):
    return render(request, 'project_list.html',)

def project_approve(request):
    return render(request, 'project_approve.html',)

def project_result(request):
    return render(request, 'project_result.html',)

def project_members(request):
    return render(request, 'project_members.html',)

def project_manage(request):
    return render(request, 'project_manage.html',)

    
