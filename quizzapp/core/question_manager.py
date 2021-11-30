from .models import *
from django.db.models import Count
import random

def get_random_questions(subcategory,numbers=10):
    count=list(QuestionModel.objects.filter(sub_category=subcategory))
    random.shuffle(count)
    return count[0:numbers]
