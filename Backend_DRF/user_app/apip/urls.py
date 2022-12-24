from django.urls import path, include
from .views import UserList, UserDetail, UserRegister, UserLogin, UserLogout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    # path('login/', TokenObtainPairView.as_view(), name='User-login'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    path('list/', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
