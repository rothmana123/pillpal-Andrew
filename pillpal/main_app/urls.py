from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('medications/', views.medications_index, name='index'),
    path('medications/<int:medication_id>/', views.medications_detail, name='detail'),
    path('medications/create/', views.MedicationsCreate.as_view(), name='medications_create'),    


]
