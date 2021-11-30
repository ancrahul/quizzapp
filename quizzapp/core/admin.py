from django.contrib import admin
from .models import *

@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display=["img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]


@admin.register(QuizzHistroy)
class QuizzHistroyAdmin(admin.ModelAdmin):
    list_display = ['room_code','user_and_score','winner',]