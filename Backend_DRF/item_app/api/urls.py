from django.urls import path
from .views import ItemListAV, ItemDetailAV, UserItemList


urlpatterns = [
    path('list/', ItemListAV.as_view(), name='item-list'),
    path('<int:pk>/', ItemDetailAV.as_view(), name='item-detail'),
    path('<int:pk>/list/', UserItemList.as_view(), name='user-item-detail'),
]

# urlpatterns = [
#     path('list/', movielist, name='item-list'),
#     path('<int:pk>', moviedetails, name='item-details'),
# ]
