from django import forms
from . models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor   
        fields = "__all__"
        exclude = ['status']
        labels = {
            "first_name": "Nombre completo",
            "last_name": "Apellidos",
            "document": "Documento",
            "address": "Dirección",
            "email": "Correo electrónico",
            "phone": "Teléfono",
            "specialty": "Especialidad"
        }
        widgets ={
            "first_name": forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del doctor'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Ingrese los apellidos del doctor'}),
            "document": forms.TextInput(attrs={'placeholder': 'Ingrese el documento del doctor'}),
            "address": forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del doctor'}),
            "email": forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico del doctor', 'type': 'email'}),
            "phone": forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono del doctor'}),       
        }
    