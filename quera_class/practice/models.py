from django.db import models
from clas.models import Class
from panel.models import Student
class Practice(models.Model):
    FILE_TYPE_CHOICE = (
        ('py', 'Python File'),
        ('txt' , 'Text File'),
        ('cpp' , 'C++ File'), 
        ('class' , 'java File'),
        ('cs', 'c# File')
    )
    class_assigned = models.ForeignKey(Class , on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.FileField(upload_to='answers/')
    answer_type = models.CharField(max_length=10 , choices=FILE_TYPE_CHOICE)
    first_time_limit = models.DurationField(blank=True , null=True)
    second_time_limit = models.DurationField(blank=True , null= True)
    submission_limit = models.PositiveIntegerField(blank=True , null=True)
    score = models.PositiveIntegerField()
    is_group = models.BooleanField(default=False)

class Submission(models.Model):
    exersice = models.ForeignKey(Practice , on_delete=models.CASCADE)
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    content = models.FileField(upload_to='submissions/')
    score_recived = models.PositiveIntegerField()
