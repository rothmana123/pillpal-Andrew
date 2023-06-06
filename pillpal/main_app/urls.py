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
    path('accounts/signup/', views.signup, name='signup'),
    path('medications/<int:medication_id>/assoc_pharmacy/<int:pharmacy_id>/', views.assoc_pharmacy, name='assoc_pharmacy'),
    path('medications/<int:medication_id>/unassoc_pharmacy/<int:pharmacy_id>/', views.unassoc_pharmacy, name='unassoc_pharmacy'),
    path('pharmacies/', views.PharmacyList.as_view(), name='pharmacies_index'),
    path('pharmacies/<int:pk>/', views.PharmacyDetail.as_view(), name='pharmacies_detail'),
    path('pharmacies/create/', views.PharmacyCreate.as_view(), name='pharmacies_create'),
    path('pharmacies/<int:pk>/update/', views.PharmacyUpdate.as_view(), name='pharmacies_update'),
    path('pharmacies/<int:pk>/delete/', views.PharmacyDelete.as_view(), name='pharmacies_delete'),
]
