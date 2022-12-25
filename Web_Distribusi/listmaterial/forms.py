from django import forms
from .models import ListModel, DistributeModel

class ListForm(forms.ModelForm):
    class Meta:
        model = ListModel
        fields = '__all__'

        labels = {
            'material_id':'Id Material',
            'nama_material':'Nama Material',
            'berat_kg':'Berat (kg)'
        }

        widgets = {
            'material_id':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Id dari material'
                }
            ),

            'nama_material':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nama material'
                }
            ),

            'berat_kg':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Berat material dalam kilogram'
                }
            ),

            'deskripsi':forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            )
        }

class DistributeForm(forms.ModelForm):
    class Meta:
        model = DistributeModel
        fields = '__all__'

        labels = {
            'material_id':'Id Material',
            'material_name':'Nama Material',
            'lini_produksi':'Lini Produksi'
        }

        widgets = {
            'material_id':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'material_name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'lini_produksi':forms.Select(
                attrs={
                    'class':'form-control'
                }
            )
        }

