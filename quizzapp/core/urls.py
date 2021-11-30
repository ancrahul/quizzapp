
from django.urls import path,include
from .views import  *


from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register("question",QuestionModelViewSet,basename="")

urlpatterns = [
    path("",home),
    path("api/",include(routers.urls)),
    path("qupload/",QuestionUploadView.as_view()),
    
]
