from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .question_manager import *
from .quizz_manager import *
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from sqlalchemy import create_engine
from .serializer import *
from .custom_pagination import QuestionListPagination
from rest_framework.parsers import *
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.decorators import action



##########  Test Code   ###########
def home(request):
    f=QuestionUploadForm()
    return render(request,"home.html",{"f":f})
    # question_set=get_random_questions("Indian History",5)
    # return HttpResponse(question_set)

#######################################
###User
#######################################

class CustomUserViewSet(ModelViewSet):
    # permission_classes =(IsAuthenticated,)    
    queryset= CustomUser.objects.all()
    serializer_class= CustomUserSerializer



class CustomUserCreate(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json)
        return Response(serializer.errors)



#######################################
###Question
#######################################
from rest_framework.decorators import api_view
import datetime
import json
from django.core.serializers import serialize


class QuestionModelViewSet(ModelViewSet):
    queryset= QuestionModel.objects.all()
    serializer_class= QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']
    pagination_class= QuestionListPagination

    @action(detail=False, methods=['GET'], name='Get_category')
    def category(self,request,pk=None):
        obj=QuestionModel.objects.values("category").distinct()
        obj_ser=QuestionCategorySerializer(obj,many=True)
        catlist={"category":[ i['category'] for i in obj_ser.data]}
        return Response(catlist)



# class QuestionCategoryView(APIView):
#     def get(self,request):
#         category_obj=QuestionModel.objects.values("category").distinct()
#         category_obj_ser=Qcatserializer(category_obj,many=True)
#         catlist={"category":[ i['category'] for i in category_obj_ser.data]}
#         return Response(catlist)


class QuestionSubCategoryView(APIView):
    def get(self,request,catname=None):
        obj=QuestionModel.objects.filter(category=self.kwargs['catname']).values("sub_category").distinct()
        obj_ser= QuestionSubCategorySerializer(obj,many=True)
        subcatlist={"sub_category":[ i['sub_category'] for i in obj_ser.data]}
        return Response(subcatlist)



class QuestionUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self,request):
        question_objects=QuestionModel.objects.all()
        serialized_question=QuestionSerializer(question_objects,many=True)
        df=pd.DataFrame(serialized_question.data)
        df.to_excel(f"question_exel/{uuid.uuid4().hex}.xls",encoding="UTF-8", engine='openpyxl', index=False)
        return Response("{data: true}")

    def post(self,request):
        question_upload_object= QuestionUpload.objects.create(exel_file_upload=request.FILES['exel_file_upload'])
        resp=save_exel_to_question_model(question_upload_object)
        return Response(resp)


##########################
#Quizz
##########################

class QuizzLogGameViewSet(ModelViewSet):
    queryset=QuizzLog.objects.all()
    serializer_class=QuizzLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category',"active_flag"]


    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(room_code=room_code_generator())
        headers = self.get_success_headers(serializer.data)
        qi=QuizzLog.objects.get(id=serializer.data["id"])
        ci=CustomUser.objects.get(id=request.user.id)
        UserQuizzScore.objects.create(user=ci,quizzlog=qi)
        return  Response(serializer.data)   

    @action(detail=False, methods=['PATCH'], name='joinquizz')
    def joinquizz(self,request):
        print(self.request.data['room_code'])
        obj=QuizzLog.objects.get(room_code=self.request.data['room_code'])
        join_quizz(self.request,obj)
        return Response({"status":f"{self.request.user} joined"})


class UserQuizzScoreViewSet(ModelViewSet):
    queryset = UserQuizzScore.objects.all()
    serializer_class = UserQuizzScoreSerializer


class LivegamelistViewSet(ModelViewSet):
    queryset = QuizzLog.objects.filter(active_flag=True)
    serializer_class = LivegameListSerializer

        


#######################################
###Accounts
#######################################

class LoginTokenObtainPairView(TokenObtainPairView):
    permission_classes=(AllowAny,)
    serializer_class= LoginTokenPairSerializer



############################################



# @api_view(['GET'])
# def get_live_quizz_api(request):
#     ser = json.loads(serialize('json',get_live_quizz()))
#     return Response(ser)

# @api_view(['POST'])
# def create_quizz_api(request):
#     ser_data = QuizzLogSerializer(data=request.data)
#     if ser_data.is_valid():
#         ser_data.user.add(request.user.id)
#         ser_data.save()
        
#         return Response({'msg': 'Game room created'})
#     return Response(ser_data.errors)



# @api_view(['GET','POST'])
# def join_quizz_api(request):
#     if request.method == 'GET':
#         obj = QuizzLog.objects.all().filter(active_flag = True)
#         serobj = QuizzLogSerializer(obj)
#         return Response(serobj.data)

#     if request.method == 'POST':
#         data = request.data
#         room_code = data['room_code']
#         join_quizz(request,room_code)
#         return Response({'success':'success'})

################################################################################



        