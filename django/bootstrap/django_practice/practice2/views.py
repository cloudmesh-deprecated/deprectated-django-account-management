from django.shortcuts import render
from django.http import HttpResponse
from mongoengine import *
from reservation.model import reservation_connect
from reservation.model import Reservation
from reservation.plot import timeline_plot


# Create your views here.

def index(request):

	connect('reservation', port = 27777)

	reservations = Reservation.objects()
	result = "<table>"
	for reservation in reservations:
        	result = result + "<tr>" 

		for attribute in reservation:
			result = result + "<td>"
			result = result + reservation[attribute]
			result = result + "</td>"

		result = result + "</tr>" + "\n"


	print 70*"D"
	print result
	print 70*"D"

	result = "</table>"
	return HttpResponse(result)











