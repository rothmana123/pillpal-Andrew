# import os
# import uuid
# import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Medication, MedicationIntake
from .forms import MedicationIntakeForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def medications_index(request):
    medications = Medication.objects.filter(user=request.user)
    return render(request, 'medications/index.html', {'medications': medications})

@login_required
def medications_detail(request, medication_id):
    medication = Medication.objects.get(id=medication_id)
    medicationintake_form = MedicationIntakeForm()
  
    context = {
        'medication': medication,
        'medicationintake_form': medicationintake_form,

    }
    return render(request, 'medications/detail.html', context)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class MedicationCreate(LoginRequiredMixin, CreateView):
    model = Medication
    fields = ['name', 'dose', 'frequency', 'warnings']
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class MedicationUpdate(LoginRequiredMixin, UpdateView):
    model = Medication
    fields = ['name', 'dose', 'frequency', 'warnings']

class MedicationDelete(LoginRequiredMixin, DeleteView):
    model = Medication
    success_url = '/medications/'

@login_required
def add_medicationintake(request, medication_id):
    form = MedicationIntakeForm(request.POST)
    if form.is_valid():
        new_medicationintake = form.save(commit=False)
        new_medicationintake.medication_id = medication_id
        new_medicationintake.save()
    return redirect('detail', medication_id=medication_id)






