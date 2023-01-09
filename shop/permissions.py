from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsSenderOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.profile.is_sender:
            return True
        else:
            return False

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            bool(request.user and request.user.is_authenticated and obj.profile == request.user)