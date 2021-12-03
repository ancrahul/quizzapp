from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields="__all__"
        # fields=["id","img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]



class RawQuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionModel
        fields=["category"]
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['category'] = instance['category']
    #     return representation 
 



class LoginTokenPairSerializer(TokenObtainPairSerializer):
    ### Inserting Addition of user info into token  ####
    @classmethod
    def get_token(cls, user):                                        
        token = super(LoginTokenPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['score'] = user.total_score
        return token



def checkempty(value):
    if value=="":
        raise serializers.ValidationError('This field is required.')
    

class CustomUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=254,validators=[checkempty])
    class Meta:
        model = CustomUser
        fields=["username","email","password"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(CustomUserSerializer, self).create(validated_data)

    
