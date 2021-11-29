from .models import *
from django.db.models import Count
import random

def get_questions(numbers):

    count=QuestionModel.objects.filter(sub_category="geomorphology.").values_list("id",flat=True)
    print(count)

    
    
