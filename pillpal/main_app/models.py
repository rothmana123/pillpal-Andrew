from django.db import models
from django.urls import reverse
from datetime import date, timezone
from django.utils.timezone import now

from django.contrib.auth.models import User


# Create your models here.

class Medication(models.Model):
    name = models.CharField(max_length=150)
    dose = models.CharField(max_length=150)
    frequency = models.PositiveBigIntegerField()
    warnings = models.TextField(max_length=300)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'medication_id': self.id})
    
    
class MedicationIntake(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

    def __str__(self):
        return f"A dose of {self.medication} was taken at {self.timestamp}"


    