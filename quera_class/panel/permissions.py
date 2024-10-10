from rest_framework.permissions import BasePermission
from .models import *

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        teacher = Teacher.objects.get(user=request.user)
        if teacher:
            return True
        else:
            return False
        
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        student = Student.objects.get(user=request.user)
        if student:
            return True
        else:
            return False
        
class IsMentor(BasePermission):
    def has_permission(self, request, view):
        mentor = Mentor.objects.get(user=request.user)
        if mentor:
            return True
        else:
            return False