
from rest_framework.permissions import BasePermission

class BlacklistPermission(BasePermission):
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        if ip_addr == '127.0.0.1':
            return True