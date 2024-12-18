from rest_framework import permissions

method2perm = {
    'GET':'view',
    'HEAD':'view',
    'OPTIONS':'view',
}

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method not in method2perm and obj.author != request.user and not request.user.is_superuser:
            return False
        return True



