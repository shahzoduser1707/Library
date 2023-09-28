from rest_framework.permissions import BasePermission

class AdminWriterPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 2 or request.user.role == 3:
            return True
        return False


class OwnerPermissionClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user.id:
            return True
        return False