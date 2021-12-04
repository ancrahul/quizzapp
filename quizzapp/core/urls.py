
from django.urls import path,include
from .views import  *


from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register("question",QuestionModelViewSet,basename="")

urlpatterns = [
    path("api/",include(routers.urls)),
    path("test/",test),
    path("test2/",test2,name="test2")

]
