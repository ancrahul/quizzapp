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
    random_id_list = random.sample(list(same_subcategory_ids_queryset),min(len(same_subcategory_ids_queryset), 1))
    random_question_queryset = QuestionModel.objects.filter(id__in = random_id_list)
    return random_question_queryset
    
def validate_answer(request):
    data = request.data
    qs_id = data['id']
    answer = data['answer']
    get_answer_from_db = QuestionModel.objects.filter(id= qs_id).values_list('correct_answer',flat=True)
    if answer in get_answer_from_db:
        return True
    else:
        return False

def update_total_score():
    # current score will be zero 
    # if user give right answer score will be +10
    # if user give wrong answer score will be -10
    # if user give no answer score will not change
    pass

def update_current_game_score(request,validate_answer,room_code):
    obj = UserQuizzScore.objects.get(quizzlog__room_code = room_code,user = request.user)
    current_score = obj.score
    if validate_answer == True:
        current_score = current_score + 10
    if validate_answer == False:
        current_score = current_score - 10
    obj.score = current_score
    obj.save()
    return "success"

def get_current_game_score(request,room_code):
    user_quiz_score = UserQuizzScore.objects.get(quizzlog__room_code=room_code, user=request.user)
    return user_quiz_score.score

def get_winner(room_code):
    winner = QuizzLog.objects.get(room_code=room_code)
    return winner.winner

def create_quizz(request):
    quiz_creator = request.user.id
    sub_category = request.data['sub_category']
    room_code = room_code_generator()
    QuizzLog.objects.create(room_code=room_code,sub_category=sub_category)
    instance = QuizzLog.objects.get(room_code=room_code)
    instance.user.add(quiz_creator)
    instance.save()


def get_live_quizz():
    live_quizz = QuizzLog.objects.all().filter(active_flag = True)
    return live_quizz

def join_quizz(request):
    data = request.data
    room_code = data['room_code']
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

