from django import forms
from . models import Appointment
from doctors.models import Doctor
from patients.models import Patient

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label='Seleccione un doctor')
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label='Seleccione un paciente')
    class Meta:
        model = Appointment
        fields = '__all__'
        labels = {
            'type_appointment': 'Tipo de cita',
            'date': 'Fecha de la cita',
            'time': 'Hora de la cita',
            'doctor': 'Doctor',
            'patient': 'Paciente',
        }
        widgets = {
            'type_appointment': forms.Select(attrs={'placeholder': 'Tipo de cita'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
        }