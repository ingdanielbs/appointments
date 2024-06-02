from django import forms
from . models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        exclude = ['status']
        labels = {
            "first_name": "Nombre del doctor",
            "last_name": "Apellido del doctor",
            "document": "Documento de identidad",
            "address": "Dirección",
            "email": "Correo electrónico",
            "phone": "Teléfono",
            "specialty": "Especialidad",
        }
        widgets ={
            "first_name": forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del doctor'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Ingrese el apellido del doctor'}),
            "document": forms.TextInput(attrs={'placeholder': 'Ingrese el documento de identidad'}),
            "address": forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del doctor'}),
            "email": forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico del doctor', 'type': 'email'}),
            "phone": forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono del doctor'}),
        }
