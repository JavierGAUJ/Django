from django.shortcuts import render

# Create your views here.

def alarmas(request):
    return HttpResponse('<h1>alarmas!<\h1>')