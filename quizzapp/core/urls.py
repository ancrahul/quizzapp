
from django.urls import path,include
from .views import  *


from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

routers=DefaultRouter()
routers.register("question",QuestionModelViewSet,basename="question")
routers.register("user",CustomUserViewSet,basename="user")
routers.register("quizzgame",QuizzLogGameViewSet,basename="quizzgame")
routers.register("livegame",LivegamelistViewSet,basename="livegame")
routers.register("quizzquestion",QuizzQuestionView,basename="quizz_question")

urlpatterns = [
    path("",home),
    path("api/",include(routers.urls)),
    path("api/qupload/",QuestionUploadView.as_view(),name='question_upload'),
    path("api/getquizzquestion",QuizzQuestionListView.as_view(),name="get_quizz_question"),
    path("api/submitanswer",SubmitAnswerView.as_view(),name="submit_answer"),
    path("api/submitquizz",SubmitQuizzView.as_view(),name="submit_quizz"),
    path("api/test",TestView.as_view(),name="test"),
    path("api/question/category/<slug:catname>/subcategory",QuestionSubCategoryView.as_view(),name='question_category'),
    path('api/login/',LoginTokenObtainPairView.as_view(),name='login'),
    path('api/registration/',CustomUserCreate.as_view(),name='registration'),
    path('api/refreshtoken/',TokenRefreshView.as_view()),
    path('api/verifytoken/',TokenVerifyView.as_view()),


    # path('live_quizz',get_live_quizz_api),
    # path('create_quizz',create_quizz_api),
    # path('join_quizz',join_quizz_api)
]
