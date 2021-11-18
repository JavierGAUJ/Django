from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms



# Create your views here.

def index(request):
    if "alarmas " not in request.session:
        request.session["alarmas"] = ['5:30', '5:35', '5:40', '5:50']
    return render(request, 'alarmas/index.html', {'alarmas':request.session["alarmas"]})

def v2(request):
    if request.methood == 'POST':
        form =FnuevaAlarma(request.POST)
        if form. is_valid():
            alarma = form.cleaned_data['alarma']
            request.session["alarmas"] += [alarma]
            return HttpResponseRedirect(reverse('alarmas:index'))
        else:
                return render(request, 'alarmas/v2.html', {'cont_form':form})
    else:
                return render(request, 'alarmas/v2.html', {'cont_form':FnuevaAlarma()})


class FnuevaAlarma(forms.form): 
    alarma = forms.CharField(label='nueva_alarma')


    # snooze = forms.Intergerfield(label='Repetir', min_value=0, max_value=10)