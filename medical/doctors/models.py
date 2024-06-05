from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    specialty = models.ForeignKey('specialties.Specialty', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
