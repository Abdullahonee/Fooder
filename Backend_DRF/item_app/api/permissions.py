from rest_framework import permissions
from user_app.models import User


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = User.objects.filter(email=request.user.email)
        return user.is_seller == False

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user