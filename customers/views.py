from rest_framework import generics

from customers.models import Customer
from customers.serializers import CustomerSerializer
# Create your views here.

class CustomersList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

