from django.contrib import admin
from .models import *

admin.site.register(Medication)
admin.site.register(MedicationIntake)
admin.site.register(Pharmacy)


