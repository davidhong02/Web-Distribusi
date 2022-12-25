from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import forms, formset_factory, modelformset_factory

from listmaterial.models import ListModel, DistributeModel
from listmaterial.forms import DistributeForm

def index (request):
    return HttpResponse("<h1> halaman ini untuk distribusi material </h1>")

def distribute2(request):
    selected_values = request.POST.getlist('chkbox[]')
    listmodels = ListModel.objects.all()
    materialid = []
    materialname = []
    initialvalue = []
    for i in selected_values:
        for j in listmodels:
            if i == j.nama_material:
                materialid.append(j.material_id)
                materialname.append(i)
            else:
                pass
    print(len(selected_values))
    for x in range(len(materialid)):
        value = {'material_id':materialid[x], 'material_name':materialname[x]}
        initialvalue.append(value)
    
    
    DistributeFormSet = formset_factory(DistributeForm, extra=len(selected_values), max_num=1)
    formset = DistributeFormSet(initial=initialvalue)  

    # upload data ke database
    length = int(request.POST.get('form-TOTAL_FORMS', False))
    for x in range (length):
        varid="form-{}-material_id".format(x)
        varname="form-{}-material_name".format(x)
        varlini="form-{}-lini_produksi".format(x)

        DistributeModel.objects.create(
            material_id = request.POST.get(varid, False),
            material_name = request.POST.get(varname, False),
            lini_produksi = request.POST.get(varlini, False)
        )
        instance = ListModel.objects.filter(material_id=request.POST.get(varid, False)).delete()
        
    context = {
            'formset':formset,
            }

    return render(request, 'distribusimaterial/distributematerial.html', context)