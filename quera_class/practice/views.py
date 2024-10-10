from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,
                                    ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import *
from panel.permissions import *
from .serializers import *


class PracticeView(ListCreateAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsTeacher , IsMentor]
        elif self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        return super(PracticeView, self).get_permissions()

class PracticeEdit(RetrieveUpdateDestroyAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [IsTeacher , IsMentor]

class RankingView(ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionRankSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["score_recived"]
    permission_classes = [IsAuthenticated]


class Grading(APIView):
    pass 


