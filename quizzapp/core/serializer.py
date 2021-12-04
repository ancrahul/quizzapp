from .models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields=["id","img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]


class JoinOrCreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizzLog
        fields = ["id","room_code","user","sub_category","winner","active_flag","created_at","started_at","completed_at"]