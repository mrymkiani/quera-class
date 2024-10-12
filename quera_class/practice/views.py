from django.shortcuts import render ,HttpResponse
import tempfile , subprocess, json , requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,
                                    ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
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


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    @action(detail=True, methods=['post'])
    def submit_code(self, request, pk=None):
        question = self.get_object()
        submission = Submission.objects.create(
            student=request.user,
            question=question,
            code=request.data.get('code')
        )
        return Response({'status': 'submission created'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def auto_grade(self, request, pk=None):
        submission = Submission.objects.get(id=request.data.get('submission_id'))
        question = submission.exersice

        result = self.run_code(submission.content, question.output , question.answer_type )

        score = 100 if result else 0
        Grade.objects.create(
            submission=submission,
            score=score
        )

        return Response({'score': score}, status=status.HTTP_200_OK)

    def run_code(self, code, expected_output, language):
        with tempfile.NamedTemporaryFile(suffix=f".{language}") as temp_code_file:
            temp_code_file.write(code.encode())
            temp_code_file.flush()
            command = []

            if language == "python":
                command = ['python', temp_code_file.name]
            elif language == "java":
                command = ['javac', temp_code_file.name]  
                subprocess.run(command) 
                command = ['java', temp_code_file.name[:-5]] 
            elif language == "javascript":
                command = ['node', temp_code_file.name]

            try:
                result = subprocess.run(command, capture_output=True, text=True)
                return result.stdout.strip() == expected_output.strip()
            except Exception as e:
                return False