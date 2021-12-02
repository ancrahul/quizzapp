from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields=["id","img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]


class LoginTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(LoginTokenPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['score'] = user.total_score
        return token



class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields=["username","email","password"]
