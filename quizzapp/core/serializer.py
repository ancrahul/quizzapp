from .models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields=["id","img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]