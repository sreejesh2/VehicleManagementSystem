from rest_framework import permissions


class SuperadminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'superadmin'

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role == 'superadmin'


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['superadmin', 'admin']

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role in ['superadmin', 'admin']


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['superadmin', 'admin', 'user']

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role in ['superadmin', 'admin', 'user']