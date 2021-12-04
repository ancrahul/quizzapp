from django.http.response import HttpResponse,JsonResponse
from rest_framework.response import Response 
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView 
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .quizz_manager import *
from .serializer import *
from rest_framework.decorators import api_view
import datetime
import json
from django.core.serializers import serialize


class QuestionModelViewSet(ModelViewSet):
    queryset= QuestionModel.objects.all()
    serializer_class= QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']

@api_view(['GET'])
def get_live_quizz_api(request):
    ser = json.loads(serialize('json',get_live_quizz()))
    return Response(ser)

@api_view(['POST'])
def create_quizz_api(request):
    data = request.data
    sub_category = data["sub_category"]
    create_quizz(request,sub_category)
    return Response({'success':'success'})

@api_view(['GET','POST'])
def join_quizz_api(request):
    if request.method == 'GET':
        # obj = QuizzLog.objects.all().filter(active_flag = True)
        # serobj = JoinOrCreateGameSerializer(obj)
        # print(serobj)
        # return Response(serobj.data)
        ser = json.loads(serialize('json',get_live_quizz()))
        return Response(ser)

    if request.method == 'POST':
        data = request.data
        room_code = data['room_code']
        join_quizz(request,room_code)
        return Response({'success':'success'})

