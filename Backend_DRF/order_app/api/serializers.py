from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    item = serializers.StringRelatedField(read_only=True)
    total_price = serializers.StringRelatedField(read_only=True)
    
    # total_price = serializers.SerializerMethodField()
    # unit_price = serializers.SerializerMethodField()
    
    # def get_total_price(self, obj):
    #     return obj.price * obj.quantity
    
    # def get_unit_price(self, obj):
    #     return obj.price
    
    class Meta:
        model = Order
        fields = ['id', 'item', 'quantity', 'total_price', 'extra', 'user']