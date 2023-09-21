from rest_framework.permissions import BasePermission

class isAuth(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class isGuest(BasePermission):
    def has_permission(self, request, view):
        return True

class isAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Administrador']).exists() or request.user.is_superuser
    
class isBodeguista(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Bodeguista']).exists()

class isCajero(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Cajero']).exists()
