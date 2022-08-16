from rest_framework import generics

from .serializers import VehicleSerializer
from .models import Vehicle

# Create your views here.
class VehiclesList(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    