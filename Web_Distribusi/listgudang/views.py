from django.shortcuts import render
from django.http import HttpResponse
from listmaterial.models import DistributeModel
# Create your views here.
def index(request):
    lini1 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 1")
    lini2 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 2")
    lini3 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 3")
    lini4 = DistributeModel.objects.filter(lini_produksi="Lini Produksi 4")

    if len(lini1) < 50:
        status1 = "Belum Penuh"
    else:
        status1= "Sudah Penuh"

    if len(lini2) < 50:
        status2 = "Belum Penuh"
    else:
        status2= "Sudah Penuh"

    if len(lini3) < 50:
        status3 = "Belum Penuh"
    else:
        status3= "Sudah Penuh"

    if len(lini4) < 50:
        status4 = "Belum Penuh"
    else:
        status4= "Sudah Penuh"




    context={
        'Title': 'Lini Produksi',
        'liniproduksi1':lini1,
        'liniproduksi2':lini2,
        'liniproduksi3':lini3,
        'liniproduksi4':lini4,
        'kapasitas1':len(lini1),
        'kapasitas2':len(lini2),
        'kapasitas3':len(lini3),
        'kapasitas4':len(lini4),
        'status1':status1,
        'status2':status2,
        'status3':status3,
        'status4':status4,
    }
    return render(request, 'listgudang/listgudang.html', context)