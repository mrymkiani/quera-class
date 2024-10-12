from django.db import models
from django.contrib.auth.models import user ,AbstractUser , PermissionsMixin
from clas.models import Class

class CustomeUser(AbstractUser , PermissionsMixin):
    USER_TYPE_CHOICE = (
        ('student' , 'Student'),
        ('teacher' , 'Teacher'),
        ('mentor' , 'Mentor')
    )
    user_type = models.CharField(max_length=10 , choices=USER_TYPE_CHOICE)