from django.db import models

# Create your models here.
class Appointment(models.Model):    
    type_appointment = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.DO_NOTHING)
    patient = models.ForeignKey('patients.Patient', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.type_appointment