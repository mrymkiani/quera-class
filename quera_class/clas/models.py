from django.db import models


class Class(models.Model):
    CLASS_TYPE_CHOICE = (
        ('public' , 'Public'),
        ('private' , 'Private')
    )
    SECURITY_TYPE_CHOICE = (
        ('password' , 'Password protect'),
        ('invite' , "Invite Only")
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    class_type = models.CharField(max_length=20 , choices=CLASS_TYPE_CHOICE)
    security_type = models.CharField(max_length=30 , choices=SECURITY_TYPE_CHOICE)
    code = models.IntegerField(blank=True , null=True)
    limit = models.PositiveIntegerField(blank=True , null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True , null=True)


class Forum(models.Model):
    CONTENT_TYPE_CHOICE = (
        ('question' , 'Question'),
        ('answer' , "Answer")
    )

    content = models.TextField()
    sender = models.ForeignKey()
    content_type = models.CharField(max_length=30 , choices=CONTENT_TYPE_CHOICE)
    refers_to = models.CharField()
    
