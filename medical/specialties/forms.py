from django import forms
from . models import Specialty


class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty   
        fields = "__all__"
        labels = {
            "name": "Nombre de la especialidad"
        }
        widgets ={
            "name": forms.TextInput(attrs={'placeholder': 'Ingrese el nombre de la especialidad'})
        }
    