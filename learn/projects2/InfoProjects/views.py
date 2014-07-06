from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from InfoProjects.models import InfoProject
from InfoProjects.serializers import InfoProjectSerializer
#from django_tables2   import RequestConfig
#from InfoProjects.models  import InfoProject
#from InfoProjects.tables import NameTable

# Create your views here.

#def info_projects(request):
	
    #info = [
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def InfoProject_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        infoprojects = InfoProject.objects.all()
        serializer = InfoProjectSerializer(infoprojects, many=True)
        return JSONResponse(serializer.data) 

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InfoProjectSerializer(data=data)
        if serializer.is_valid():
    	    serializer.save()
    	    return JSONResponse(serializer.data, status=201)
    	return JSONResponse(serializer.errors, status=400)
        
        
@csrf_exempt
def InfoProject_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Infoproject = InfoProject.objects.get(pk=pk)
    except InfoProject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectInfoSerializer(Infoproject)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InfoProjectSerializer(Infoproject, data=data)
        if serializer.is_valid():
    	    serializer.save()
    	    return JSONResponse(serializer.data)
    	return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Infoproject.delete()
        return HttpResponse(status=204)

	
     		#]

#table = NameTable(info)
#RequestConfig(request).configure(table)
#return render(request, "template_example.html", {'table': table})



