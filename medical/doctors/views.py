from django.shortcuts import render, redirect
from . forms import DoctorForm
from django.contrib import messages
from doctors.models import Doctor
from specialties.models import Specialty

# Create your views here.
def doctors(request):
    form = DoctorForm(request.POST or None)
    doctors = Doctor.objects.all()
    specialties = Specialty.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Doctor registrado con éxito.')
            return redirect('doctors')
        except:
            messages.error(request, 'Ocurrió un error al registrar el doctor.')
            return redirect('doctors')    
    return render(request, "doctors/index.html", {'form': form, 'doctors':doctors, 'specialties':specialties})

def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    try:
        doctor.delete()
        messages.success(request, 'Doctor eliminado con éxito.')
        return redirect('doctors')
    except:
        messages.error(request, 'Ocurrió un error al eliminar el doctor.')
        return redirect('doctors')    

def edit_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Doctor actualizado con éxito.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al actualizar el doctor: {e}')
            return redirect('doctors')
    return render(request, 'doctors/edit.html', {'form': form})