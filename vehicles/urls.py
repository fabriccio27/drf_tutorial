from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('api/vehicles/', views.VehiclesList.as_view(), name='vehicles-list')
]
