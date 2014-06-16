from django.shortcuts import render
from django_tables2   import RequestConfig
from practice1.models  import Person
import django_tables2 as tables
#from practice1.tables  import PersonTable
#from django.http import HttpResponse



# Create your views here.

#def index(request):

	#result = "hello world"

	#return HttpResponse(result)





data = [
    {"name": "Bradley"},
    {"name": "Stevie"},
]

class NameTable(tables.Table):
    name = tables.Column()

table = NameTable(data)



def people(request):
	#table = PersonTable(Person.objects.all())
    	#RequestConfig(request).configure(table)
   	return render(request, 'people.html', {'table': table})








#return render(request, "people.hmtl", {"people": Person.objects.all()})

	



