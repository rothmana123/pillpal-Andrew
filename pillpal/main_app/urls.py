from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('medications/', views.medications_index, name='index'),
    path('medications/<int:medication_id>/', views.medications_detail, name='detail'),
    path('medications/create/', views.MedicationCreate.as_view(), name='medications_create'),   
    path('medications/<int:pk>/update/', views.MedicationUpdate.as_view(), name='medications_update'), 
    path('medications/<int:pk>/delete/', views.MedicationDelete.as_view(), name='medications_delete'), 
    path('medications/<int:medication_id>/add_medicationintake/', views.add_medicationintake, name='add_medicationintake'),



]
