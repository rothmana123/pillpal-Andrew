# import os
# import uuid
# import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Medication, MedicationIntake
from .forms import MedicationIntakeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def medications_index(request):
    medications = Medication.objects.all()
    return render(request, 'medications/index.html', {'medications': medications})

def medications_detail(request, medication_id):
    medication = Medication.objects.get(id=medication_id)
    medicationintake_form = MedicationIntakeForm()
  
    context = {
        'medication': medication,
        'medicationintake_form': medicationintake_form,

    }
    return render(request, 'medications/detail.html', context)

class MedicationCreate(CreateView):
    model = Medication
    fields = '__all__'

class MedicationUpdate(UpdateView):
    model = Medication
    fields = '__all__'

class MedicationDelete(DeleteView):
    model = Medication
    success_url = '/medications/'

def add_medicationintake(request, medication_id):
    form = MedicationIntakeForm(request.POST)
    if form.is_valid():
        new_medicationintake = form.save(commit=False)
        new_medicationintake.medication_id = medication_id
        new_medicationintake.save()
    return redirect('detail', medication_id=medication_id)






