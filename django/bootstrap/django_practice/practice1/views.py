from django.shortcuts import render
from django_tables2   import RequestConfig
from practice1.models  import Person
from practice1.tables  import PersonTable
#from django.http import HttpResponse



# Create your views here.

#def index(request):

	#result = "hello world"

	#return HttpResponse(result)

def people(request):
	table = PersonTable(Person.objects.all())
    	RequestConfig(request).configure(table)
   	return render(request, 'people.html', {'table': table})








#return render(request, "people.hmtl", {"people": Person.objects.all()})

	



