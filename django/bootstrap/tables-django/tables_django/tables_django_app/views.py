from django.shortcuts import render
#from django.db import models
from .models import Person
# Create your views here.

#def index(request):
	#return render(request, 'tables_django_example.html',)

def people(request):
	return render(request, "tables_django_example.html", {"people": Person.objects.all()})
	#return render(request, "tables_django_example.html",)
