from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.



def holaDjango(request):
    return HttpResponse('<h1>hola Django!<\h1>')

def pepe(request):
    return HttpResponse('hola pepe!')

def holatu(request, nombre):
    return HttpResponse(f'hola {nombre.capitalize()}!')

def indice(request):
    return render(request, 'principal/index.html')