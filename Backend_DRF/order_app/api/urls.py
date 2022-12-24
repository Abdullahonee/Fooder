from django.urls import path
from .views import OrderList, OrderDetail, OrderCreate

urlpatterns = [
    path('<int:pk>/orders/', OrderList.as_view(), name='seller-order-list'),
    path('list/', OrderList.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('<int:pk>/order-create/', OrderCreate.as_view(), name='order-create'),
]