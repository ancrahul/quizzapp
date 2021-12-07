
from django.urls import path,include
from .views import  *


from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register("question",QuestionModelViewSet,basename="")

urlpatterns = [
    path("api/",include(routers.urls)),
    path('live_quizz',get_live_quizz_api),
    path('create_quizz',create_quizz_api),
    path('join_quizz',join_quizz_api),
    path('question',question),
    path('current_game_score',update_current_score),
    path('winner',determine_winner_view),
    path('update_total_score',update_total_score_view),


]