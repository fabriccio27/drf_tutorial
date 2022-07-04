from django.urls import path
from customers import views

urlpatterns = [
    path('api/customers/', views.CustomersList.as_view(), name='customers-list')
]
