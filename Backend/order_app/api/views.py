from .serializers import OrderSerializer
from ..models import Order
from item_app.models import ItemList
from rest_framework import generics

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        item = ItemList.objects.get(pk=pk)
        item.order_count+=1
        quantity = serializer.validated_data['quantity']
        item.total_available -= quantity
        total_price = quantity * item.price
        item.save()
        user = self.request.user
        user.save()
        serializer.save(user=user, item=item, total_price=total_price)
        

class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        # pk = self.kwargs.get(pk=pk)
        return Order.objects.all()
    
    
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_destroy(self, instance):
        item = instance.item
        item.order_count-=1
        item.save()
        user = item.user
        user.order_count-=1
        user.save()
        instance.delete()