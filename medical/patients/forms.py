from django import forms
from . models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient   
        fields = "__all__"
        exclude = ['status']
        labels = {
            "first_name": "Nombre del paciente",
            "last_name": "Apellido del paciente",
            "document": "Documento de identidad",
            "address": "Dirección",
            "email": "Correo electrónico",
            "phone": "Teléfono",
            "date_of_birth": "Fecha de nacimiento"            
        }
        widgets ={
            "first_name": forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del paciente'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Ingrese el apellido del paciente'}),
            "document": forms.TextInput(attrs={'placeholder': 'Ingrese el documento de identidad'}),
            "address": forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del paciente'}),
            "email": forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico del paciente', 'type': 'email'}),
            "phone": forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono del paciente'}),
            "date_of_birth": forms.DateInput(attrs={'placeholder': 'Ingrese la fecha de nacimiento del paciente', 'type': 'date'}),

        }
        
    