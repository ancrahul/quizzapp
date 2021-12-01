from django.contrib import admin
from .models import *

@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display=["img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]


class TermInlineAdmin(admin.TabularInline):
    model = QuizzLog.user.through


@admin.register(QuizzLog)
class QuizzLogAdmin(admin.ModelAdmin):
    list_display = ('room_code','winner')
    inlines = (TermInlineAdmin,)

    # def get_user(self,obj):
    #     return "\n".join([u.username for u in obj.user.all()])


@admin.register(QuizzUserScore)
class QuizzUserScoreAdmin(admin.ModelAdmin):
    list_display = ['user','quizzlog','score']
