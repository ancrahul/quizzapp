from .models import  *
import random

def get_random_ten_question():
    same_subcategory_ids_queryset = QuestionModel.objects.filter(sub_category = 'Geolocation').values_list('id',flat=True)
    random_id_list = random.sample(list(same_subcategory_ids_queryset),min(len(same_subcategory_ids_queryset), 5))
    random_question_queryset = QuestionModel.objects.filter(id__in = random_id_list)
    
    

def store_questions():
    pass

def validate_answer(answer):
    pass

def update_score():
    pass

def get_winner():
    pass