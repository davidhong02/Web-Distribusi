# Generated by Django 4.1.3 on 2022-12-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listmaterial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_id', models.CharField(max_length=10)),
                ('material_name', models.CharField(max_length=255)),
                ('tanggal_distribusi', models.DateTimeField(auto_now_add=True)),
                ('lini_produksi', models.CharField(choices=[('Lini Produksi 1', 'Lini Produksi 1'), ('Lini Produksi 2', 'Lini Produksi 2'), ('Lini Produksi 3', 'Lini Produksi 3'), ('Lini Produksi 4', 'Lini Produksi 4')], max_length=255)),
            ],
        ),
    ]