from django.shortcuts import render,redirect,HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .question_manager import *
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from sqlalchemy import create_engine
from .serializer import *

class QuestionModelViewSet(ModelViewSet):
    queryset= QuestionModel.objects.all()
    serializer_class= QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'sub_category']





def home(request):
    f=QuestionUploadForm()
    return render(request,"home.html",{"f":f})
    # question_set=get_random_questions("Indian History",5)
    # return HttpResponse(question_set)

import uuid

class QuestionUploadView(APIView):
    def get(self,request):
        question_objects=QuestionModel.objects.all()
        serialized_question=QuestionSerializer(question_objects,many=True)
        df=pd.DataFrame(serialized_question.data)
        print(df)
        df.to_excel(f"question_exel/{uuid.uuid4}.xls",encoding="UTF-8", engine='openpyxl', index=False)
        return Response("{data: true}")

    def post(self,request):
        qobj=QuestionUpload.objects.all()
        qobj.delete()

        question_upload_object= QuestionUpload.objects.create(exel_file_upload=request.FILES['exel_file_upload'])
        df = pd.read_excel(f"{settings.BASE_DIR}/{question_upload_object.exel_file_upload}",engine='openpyxl')
        for index, row in df.iterrows():
            qobj=QuestionModel()
            qobj.img_question=row["img_question"]
            qobj.question=row["question"]
            qobj.option1=row["option1"]
            qobj.option2=row["option2"]
            qobj.option3=row["option3"]
            qobj.option4=row["option4"]
            qobj.correct_answer=row["correct_answer"]
            qobj.category=row["category"]
            qobj.sub_category=row["sub_category"]
            qobj.save()
            print(row['id'])
        # user = settings.DATABASES['default']['USER']
        # password = settings.DATABASES['default']['PASSWORD']
        # database_name = settings.DATABASES['default']['NAME']
        # database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
        # user=user,
        # password=password,
        # database_name=database_name,    
        # )
        # engine = create_engine(database_url, echo=False)
        # df.to_sql(QuestionModel,con=engine,if_exists='append',index=False)
        print(df)
        print(request.FILES)
        return Response("{data: sucess}")