from .models import *
from django.db.models import Count
import random
import pandas as pd
from django.conf import settings

def get_random_questions(subcategory,numbers=10):
    count=list(QuestionModel.objects.filter(sub_category=subcategory))
    random.shuffle(count)
    return count[0:numbers]


def get_random_questions_id(subcategory,room_code,numbers=10):
    count=list(QuestionModel.objects.filter(sub_category=subcategory).values_list("id",flat=True))
    random.Random(room_code).shuffle(count)
    return count[0:numbers]




def save_exel_to_question_model(question_upload_object):
    df = pd.read_excel(f"{settings.BASE_DIR}/{question_upload_object.exel_file_upload}",index_col=0)
    ####### using loop saving one object at a time #########
    for index, row in df.iterrows():
        qobj=QuestionModel()
        qobj.img_question=str(row["img_question"])
        qobj.question=row["question"]
        qobj.option1=row["option1"]
        qobj.option2=row["option2"]
        qobj.option3=row["option3"]
        qobj.option4=row["option4"]
        qobj.correct_answer=row["correct_answer"]
        qobj.category=row["category"]
        qobj.sub_category=row["sub_category"]
        qobj.save()


        ####### Directly appending the data to postgres database###########
            
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
        # print(request.FILES)
    return {'status':'sucess'}


    
