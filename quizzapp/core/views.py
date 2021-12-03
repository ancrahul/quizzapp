from django.shortcuts import render,redirect,HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .question_manager import *
import uuid
# import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from sqlalchemy import create_engine
from .serializer import *
from .custom_pagination import QuestionListPagination
from rest_framework.parsers import *

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView



##########  Test Code   ###########
def home(request):
    f=QuestionUploadForm()
    return render(request,"home.html",{"f":f})
    # question_set=get_random_questions("Indian History",5)
    # return HttpResponse(question_set)

#######################################


class CustomUserViewSet(ModelViewSet):
    queryset= CustomUser.objects.all()
    serializer_class= CustomUserSerializer


class QuestionCategoryViewSet(ModelViewSet):
    queryset= QuestionModel.objects.values("category").distinct()
    serializer_class= RawQuestionCategorySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category', 'sub_category']
    # pagination_class= QuestionListPagination


class QuestionModelViewSet(ModelViewSet):
    queryset= QuestionModel.objects.all()
    serializer_class= QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']
    pagination_class= QuestionListPagination

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class LoginTokenObtainPairView(TokenObtainPairView):
    permission_classes=(AllowAny,)
    serializer_class= LoginTokenPairSerializer
    







class QuestionUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self,request):
        question_objects=QuestionModel.objects.all()
        serialized_question=QuestionSerializer(question_objects,many=True)
        df=pd.DataFrame(serialized_question.data)
        # print(df)
        df.to_excel(f"question_exel/{uuid.uuid4}.xls",encoding="UTF-8", engine='openpyxl', index=False)
        return Response("{data: true}")

    def post(self,request):
        file_obj = request.data
        print(file_obj)
        question_upload_object= QuestionUpload.objects.create(exel_file_upload=request.FILES['exel_file_upload'])
        resp=save_exel_to_question_model(question_upload_object)
        return Response(resp)