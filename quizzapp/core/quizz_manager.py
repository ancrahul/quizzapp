# from core.models import UserQuizzScore, QuestionModel
from .models import *
import random
import secrets
import string
import datetime
from django.utils import timezone
from django.db.models import Sum


def room_code_generator(charstring=string.ascii_lowercase + string.digits):
    return ''.join(secrets.choice(charstring) for i in range(10))


def join_quizz(request):
    room_code = request.data['room_code']
    obj=QuizzLog.objects.get(room_code=room_code)
    quiz_joiner = request.user.id
    join_time = timezone.now()
    obj.user.add(quiz_joiner)
    obj.started_at = join_time
    obj.active_flag = False
    obj.save()



def update_total_score(request):
    curret_user_score_list = UserQuizzScore.objects.filter(user=request.user    ).aggregate(Sum('score'))
    instance=CustomUser.objects.get(id = request.user.id)
    instance.total_score=curret_user_score_list['score__sum']
    instance.save()
    return "success"



def update_current_game_score(request,validate_answer):
    room_code = request.data['room_code']
    obj = UserQuizzScore.objects.get(
        quizzlog__room_code = room_code,
        user = request.user
        )
    current_score = obj.score
    if validate_answer == True:
        current_score = current_score + 10
    if validate_answer == False:
        current_score = current_score - 10
    obj.score = current_score
    obj.save()
    return current_score


def validate_answer(request):
    data = request.data
    qs_id = data['question_id']
    answer = data['answer']
    get_answer_from_db = QuestionModel.objects.get(id= qs_id).correct_answer
    resp_updated_score = update_current_game_score(request,validate_answer = (answer == get_answer_from_db))
    return resp_updated_score



def determine_winner(request):
    data = request.data['room_code']
    obj = UserQuizzScore.objects.filter(quizzlog__room_code = data).values_list('score',flat=True)
    completed_at_obj = UserQuizzScore.objects.filter(quizzlog__room_code = data)
    if obj[0] == obj[1]:
        completed_at_obj.completed_at = timezone.now()
        winner_dict = {'winner':"Tie Game"}
        return winner_dict
    else:    
        winner_score = max(obj)
        winner_obj = UserQuizzScore.objects.get(
            quizzlog__room_code = data,
            score = winner_score)
        winner = winner_obj.user.username
        winner_score = winner_obj.score
        completed_at_obj.completed_at = timezone.now()
        winner_dict = {'winner':winner,'winner_score':winner_score}
        return winner_dict