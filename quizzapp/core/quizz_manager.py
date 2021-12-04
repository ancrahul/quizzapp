from .models import  *
import random
import secrets
import string
import datetime
from django.utils import timezone



def room_code_generator(charstring=string.ascii_lowercase+string.digits):
    return ''.join(secrets.choice(charstring)for i in range(10))


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

def update_total_score():
    # current score will be zero 
    # if user give right answer score will be +10
    # if user give wrong answer score will be -10
    # if user give no answer score will not change
    pass

def update_current_game_score():
    current_score = 0
    if validate_answer == True:
        current_score = current_score + 10
    if validate_answer == False:
        current_score = current_score - 10
    update = QuizzLog.objects.get(room_code = '210AS')
    update.user_and_score['user1'] = 50
    update.save()

def get_winner(room_code):
    winner_list = QuizzLog.objects.filter(room_code=room_code).values_list('winner',flat = True)
    winner = winner_list[0]
    print(winner)

def create_quizz(request,sub_category):
    quiz_creator = request.user.id
    room_code = room_code_generator()
    QuizzLog.objects.create(room_code=room_code,sub_category=sub_category)
    instance = QuizzLog.objects.get(room_code=room_code)
    instance.user.add(quiz_creator)
    instance.save()



def get_live_quizz():
    live_quizz = QuizzLog.objects.all().filter(active_flag = True)
    return live_quizz

def join_quizz(request,room_code):
    # 2nd user, started time, room code to join, active_flag=of
    # get_live_quizz()
    quiz_joiner = request.user.id
    join_time = timezone.now() 
    instance = QuizzLog.objects.get(room_code=room_code)
    instance.user.add(quiz_joiner)
    instance.started_at = join_time
    instance.active_flag = False
    instance.save()
# ------------------------------------------------------------------------------------------------------

def get_distinct_subcategory():
    distinct_subcategory = QuestionModel.objects.all().values_list('sub_category',flat=True).distinct()
    return distinct_subcategory

