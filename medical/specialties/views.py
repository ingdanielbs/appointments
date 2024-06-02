from django.shortcuts import render, redirect
from . forms import SpecialtyForm
from django.contrib import messages
from specialties.models import Specialty

# Create your views here.
def specialties(request):
    form = SpecialtyForm(request.POST or None)
    specialties = Specialty.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Especialidad registrada con éxito.')
            return redirect('specialties')
        except:
            messages.error(request, 'Ocurrió un error al registrar la especialidad.')
            return redirect('specialties')    
    return render(request, "specialties/index.html", {'form': form, 'specialties':specialties})

def delete_specialty(request, id):
    specialty = Specialty.objects.get(id=id)
    try:
        specialty.delete()
        messages.success(request, 'Especialidad eliminada con éxito.')
        return redirect('specialties')
    except:
        messages.error(request, 'Ocurrió un error al eliminar la especialidad.')
        return redirect('specialties')
    

def edit_specialty(request, id):
    specialty = Specialty.objects.get(id=id)
    form = SpecialtyForm(request.POST or None, instance=specialty)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Especialidad actualizada con éxito.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al actualizar la especialidad: {e}')
            return redirect('specialties')
    return render(request, 'specialties/edit.html', {'form': form})
   
    