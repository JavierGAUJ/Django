from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'dia/index.html', {
        'esviernes': datetime.today().isoweekday() == 5
    })
