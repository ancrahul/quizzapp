from django.shortcuts import render,redirect,HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .question_manager import *

from .serializer import *

class QuestionModelViewSet(ModelViewSet):
    queryset= QuestionModel.objects.all()
    serializer_class= QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']





def home(request):
    question_set=get_random_questions("Indian History",5)
    return HttpResponse(question_set)