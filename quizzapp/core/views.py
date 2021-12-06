from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .quizz_manager import *
from .serializer import *
from rest_framework.decorators import api_view
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
        join_quizz(request)
        return Response({'success':'success'})


@api_view(['GET','POST'])
def question(request):
    if request.method == 'GET':
        ser = json.loads(serialize('json',get_random_ten_question()))
        return Response(ser)
    if request.method == 'POST': 
        return Response(validate_answer(request))


@api_view(['GET','POST'])
def update_current_score(request):
    if request.method == 'GET':
        a = update_current_game_score(request,validate_answer = False)
        return Response(a)
    # if request.method == 'POST':
    #     update_current_game_score(request,True)
