from django.shortcuts import render, redirect
from . forms import PatientForm
from django.contrib import messages
from patients.models import Patient

# Create your views here.
def patients(request):
    form = PatientForm(request.POST or None)
    patients = Patient.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Paciente registrado con éxito.')
            return redirect('patients')
        except:
            messages.error(request, 'Ocurrió un error al registrar el paciente.')
            return redirect('patients')    
    return render(request, "patients/index.html", {'form': form, 'patients':patients})

def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    try:
        patient.delete()
        messages.success(request, 'Paciente eliminado con éxito.')
        return redirect('patients')
    except:
        messages.error(request, 'Ocurrió un error al eliminar el paciente.')
        return redirect('patients')    

def edit_patient(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Paciente actualizado con éxito.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al actualizar el paciente: {e}')
            return redirect('patients')
    return render(request, 'patients/edit.html', {'form': form})