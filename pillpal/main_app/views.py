# import os
# import uuid
# import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Medication, MedicationIntake
# from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def medications_index(request):
    medications = Medication.objects.all()
    return render(request, 'medications/index.html', {'medications': medications})

