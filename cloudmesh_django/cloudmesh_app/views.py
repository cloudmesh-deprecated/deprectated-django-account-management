from django.shortcuts import render

def index(request):
        return render(request, 'index.html',)

def list(request):
        return render(request, 'list.html',)

def project_apply(request):
        return render(request, 'project_apply.html',)

def user_apply(request):
        return render(request, 'user_apply.html',)

    
