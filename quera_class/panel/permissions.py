from rest_framework.permissions import BasePermission
from .models import *

class IsClassTeacher(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            class_instance = view.get_object()  
            return class_instance.teacher == request.user
        except AttributeError:
            return False  
        
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if self.request.user.user_type == "student":
            return True
        else:
            return False
        
class IsMentor(BasePermission):
    def has_permission(self, request, view):
        if self.request.user.user_type == "mentor":
            return True
        else:
            return False