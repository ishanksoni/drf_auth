from rest_framework import permissions

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsOwnerOrReadOnly(permissions.BasePermission):
    msg = 'You must be owner of page!'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user