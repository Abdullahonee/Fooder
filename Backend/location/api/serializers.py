from rest_framework import serializers
from ..models import LocationDist, Locations

class LocationDistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LocationDist
        fields = "__all__"
        
    
class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Locations
        fields = "__all__"
   