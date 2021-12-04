
from django.urls import path,include
from .views import  *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

routers=DefaultRouter()
routers.register("question",QuestionModelViewSet,basename="question")
routers.register("user",CustomUserViewSet,basename="user")

urlpatterns = [
    path("",home),
    path("api/",include(routers.urls)),
    path("api/qupload/",QuestionUploadView.as_view(),name='question_upload'),
    path("api/question/category/<slug:catname>/subcategory",QuestionSubCategoryView.as_view(),name='question_category'),
    path('api/login/',LoginTokenObtainPairView.as_view(),name='login'),
    path('api/registration/',CustomUserCreate.as_view(),name='registration'),
    path('api/refreshtoken/',TokenRefreshView.as_view()),
    path('api/verifytoken/',TokenVerifyView.as_view()) 
]


