from rest_framework import generics
from .serializers import LocationSerializer
from ..models import Locations

class LocationList(generics.ListAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer