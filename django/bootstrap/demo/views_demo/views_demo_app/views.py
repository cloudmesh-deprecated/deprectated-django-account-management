from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

# Create your views here.

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_time.html')
	html = t.render(Context({ 'current_date': now}))
	return HttpResponse(html) 
