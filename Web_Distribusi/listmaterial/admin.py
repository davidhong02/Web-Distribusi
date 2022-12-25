from django.contrib import admin
from .models import ListModel, DistributeModel
# Register your models here.

class listmaterialadmin(admin.ModelAdmin):
    list_display = ('material_id', 'nama_material', 'tanggal_masuk')

class listdistribusiadmin(admin.ModelAdmin):
    list_display = ('material_id', 'material_name', 'lini_produksi', 'tanggal_distribusi')

admin.site.register(ListModel, listmaterialadmin)
admin.site.register(DistributeModel, listdistribusiadmin)