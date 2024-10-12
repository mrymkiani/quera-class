from .models import *
from rest_framework.serializers import ModelSerializer

class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"