from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include('item_app.api.urls')),
    path('review/', include('review_app.api.urls')),
    path('user/', include('user_app.api.urls')),
    path('order/', include('order_app.api.urls')),
    path('search/', include('finder.api.urls')),
    path('location/', include('location.api.urls')),
    
    # path('api-auth/', include('rest_framework.urls')),
]
