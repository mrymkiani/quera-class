from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,
                                    ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import *
from panel.permissions import *
#from .serializers import *





