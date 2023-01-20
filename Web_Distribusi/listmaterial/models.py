from django.db import models

# Create your models here.

class ListModel(models.Model):
    material_id = models.CharField(max_length=10)
    nama_material = models.CharField(max_length=255)
    tanggal_masuk = models.DateTimeField(auto_now_add=True)
    berat_kg = models.FloatField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_material

class DistributeModel(models.Model):
    material_id = models.CharField(max_length=10)
    material_name = models.CharField(max_length=255)
    tanggal_distribusi = models.DateTimeField(auto_now_add=True)
    PILIHAN = (
        ('Lini Produksi 1', 'Lini Produksi 1'),
        ('Lini Produksi 2', 'Lini Produksi 2'),
        ('Lini Produksi 3', 'Lini Produksi 3'),
        ('Lini Produksi 4', 'Lini Produksi 4'),
    )
    lini_produksi = models.CharField(max_length=255,choices=PILIHAN)

    def __str__(self):
        return self.material_name