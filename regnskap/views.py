# Create your views here.
## standard includes
import os
## my files import
from regnskap import models
from regnskap import forms
## django import
from django.shortcuts import render_to_response


def default(request):
    bilag_list = models.Bilag.objects.all()
    return render_to_response('default.html',{'bilag_list': bilag_list})

def registerform(request):
    konto_plan = models.Konto.objects.all()
    files = os.listdir(os.path.join('/','var','www','django_regnskap'))
    return render_to_response('form.html',{'files': files})
    
def registerAction(request):
    pass

def registrerBilagForm(request):
    if(request.method == 'POST'):
        form = forms.BilagForm(request.POST)
        if form.is_valid():
            ##process data
            
            return HttpResponseRedirect(request.get_full_path())
    else:
        form = forms.BilagForm()
    return render_to_response('bilagRegistrering.html',{
        'form': form,
        'url' : request.get_full_path(),
    })
    