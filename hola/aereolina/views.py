from django.shortcuts import render
from .models import flight

# Create your views here.

def index (request):
   return render(request, 'aereolina/index.html', {
      "flights": flight.objects.all()
   })
def flight (request, flight_id):
   flight = flight.objects.get (id=flight_id)
   return render(request, 'aereolina/flight.html', {
      'flight':flight
   })
