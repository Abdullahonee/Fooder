from rest_framework import serializers
from ..models import User
from order_app.api.serializers import OrderSerializer
from item_app.api.serializers import ItemListSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'style': {'input_type': 'password'}, 'write_only': True}
        }
        
class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'style': {'input_type': 'password'}, 'write_only': True}
        }
        
class UserSerializer(serializers.ModelSerializer):
    items = ItemListSerializer(many=True, read_only=True)
    orders = OrderSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'style': {'input_type': 'password'}, 'write_only': True}
        }