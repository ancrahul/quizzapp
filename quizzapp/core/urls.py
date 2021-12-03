
from django.urls import path,include
from .views import  *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

routers=DefaultRouter()
routers.register("question",QuestionModelViewSet,basename="question")
routers.register("category",QuestionCategoryViewSet,basename="category")
routers.register("registration",CustomUserViewSet,basename="registration")

urlpatterns = [
    path("",home),
    path("api/",include(routers.urls)),
    path("qupload/",QuestionUploadView.as_view()),
    path('login/',LoginTokenObtainPairView.as_view(),name='login'),
    path('refreshtoken/',TokenRefreshView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view()) 
]


