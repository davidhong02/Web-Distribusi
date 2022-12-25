from django.shortcuts import render
from django.http import HttpResponse
from listmaterial.models import DistributeModel
# Create your views here.
def index(request):
    lini1 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 1")
    lini2 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 2")
    lini3 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 3")
    lini4 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 4")
    context={
        'Title': 'Lini Produksi',
        'liniproduksi1':lini1,
        'liniproduksi2':lini2,
        'liniproduksi3':lini3,
        'liniproduksi4':lini4,
    }
    return render(request, 'listgudang/listgudang.html', context)