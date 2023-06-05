from django.forms import ModelForm
from .models import MedicationIntake

class MedicationIntakeForm(ModelForm):
  class Meta:
    model = MedicationIntake
    exclude = ['medication']