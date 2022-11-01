from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import VehicleSerializer
from .models import Vehicle

# Create your views here.
class VehiclesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    