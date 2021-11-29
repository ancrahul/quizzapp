from .models import  *
import random

def get_random_ten_question():
    same_subcategory_ids_queryset = QuestionModel.objects.filter(sub_category = 'Geolocation').values_list('id',flat=True)
    random_id_list = random.sample(list(same_subcategory_ids_queryset),min(len(same_subcategory_ids_queryset), 5))
    random_question_queryset = QuestionModel.objects.filter(id__in = random_id_list)
    # print(random_id_list)
    
def validate_answer(id,answer):
    get_answer_from_db = QuestionModel.objects.filter(id= id).values_list('correct_answer',flat=True)
    if answer in get_answer_from_db:
        print('True')
    else:
        print('False')

def update_score():
    pass

def get_winner():
    pass