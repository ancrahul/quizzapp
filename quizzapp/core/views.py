from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .quizz_manager import *
from .serializer import *
from rest_framework.decorators import api_view


@api_view(['GET'])
def test(request):
    # get_random_ten_question()
    validate_answer(1,'Affrica')
    return HttpResponse("test run")

class QuestionModelViewSet(ModelViewSet):
    queryset= QuestionModel.objects.all()
    serializer_class= QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']