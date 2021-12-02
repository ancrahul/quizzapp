from django.contrib import admin
from .models import *

@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display=["img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]


@admin.register(QuestionUpload)
class QuestionUploadAdmin(admin.ModelAdmin):
    list_display=['id',"exel_file_upload"]


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
admin.site.register(CustomUser, CustomUserAdmin)
