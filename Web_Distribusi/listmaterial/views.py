from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import forms, formset_factory, modelformset_factory

from .models import ListModel, DistributeModel
from .forms import ListForm, DistributeForm

# Create your views here.
def index(request):
    listmodels = ListModel.objects.all()
    
    context = {
        'page_title':'List Material',
        'heading':'List Material',
        'daftar_material':listmodels,
    }
    return render(request, 'listmaterial/index.html', context)


def create(request):
    listform = ListForm(request.POST or None)
    if request.method == 'POST':
        if listform.is_valid():
            listform.save()
            
            return redirect('/listmaterial')

    context = {
        'page_title':'Tambah Material',
        'heading':'Tambah Material',
        'form_tambah':listform,
    }
    return render(request, 'listmaterial/create.html', context)

