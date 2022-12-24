from django.urls import path
from .views import FindList


urlpatterns = [
    path('', FindList.as_view(), name='find-list'),
]