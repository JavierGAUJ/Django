from django.shortcuts import render

alarmas =['5:30', '5:35', '5:40', '5:50']

# Create your views here.

def alarmas(request):
    return render(request, 'alarmas/index.html', {'alarmas':alarmas})

def v2(request):
    return render(request, 'alarmas/v2.html')