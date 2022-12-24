from django.urls import path
from .views import ReviewList, ReviewDetail, ReviewCreate


urlpatterns = [
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/list/', ReviewList.as_view(), name='review-list'),
    path('reviewlist/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]


