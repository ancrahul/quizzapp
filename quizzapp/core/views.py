from django.http.response import HttpResponse
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


def test(request):
    # get_random_ten_question()
    # validate_answer(1,'Affrica')
    # get_winner('210AS')
    # update_score()
    # room = room_code_generator()
    # print(room)
    subcategory = get_distinct_subcategory()
    online_game = User.objects.values_list('username',flat=True)
    context = {
        "online_game" : online_game,
        "subcategory" : subcategory,
    }
    return render(request,"base.html",context) 

def test2(request):
    # create_quizz(request,sub_category = 'history')
    join_quizz(request)
    return HttpResponse('done')

class QuestionModelViewSet(ModelViewSet):
    queryset= QuestionModel.objects.all()
    serializer_class= QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']

# class QuizzJoinAndCreate(APIView):
#     serializer_class = JoinSerializer

#     def get(self):
#         join_object = Join.objects.all()


    # def post(self, request, *args, **kwargs):
