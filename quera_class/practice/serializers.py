from .models import *
from rest_framework.serializers import ModelSerializer


class PracticeSerializer(ModelSerializer):
    class Meta:
        model = Practice
        fields = "__all__"


class SubmissionRankSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ['student' , 'score_recived']
        
class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"