from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from .quizz_manager import *

############ Question Realted Serializers #############

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields="__all__"
        # fields=["id","img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]


class QuestionCategorySerializer(serializers.Serializer):
    category = serializers.CharField()

class QuestionSubCategorySerializer(serializers.Serializer):
    sub_category = serializers.CharField()



class UserQuizzScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserQuizzScore
        fields=["user","score","quizzlog"]



############ Accoounts Realted Serializers #############

def checkempty(value):  ####validator#######
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




class LoginTokenPairSerializer(TokenObtainPairSerializer):
    ### Inserting Addition of user info into token  ####
    @classmethod
    def get_token(cls, user):
        token = super(LoginTokenPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        return token





####### Quizz Related Serializer ##########

class QuizzLogSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    class Meta:
        model = QuizzLog
        fields = ["id","room_code","category","sub_category","winner","active_flag","created_at","started_at","completed_at","users"]
        # fields="__all__"

    def get_users(self, obj):
        """obj is a Member instance. Returns list of dicts"""
        qset = UserQuizzScore.objects.filter(quizzlog=obj)
        return [UserQuizzScoreSerializer(m).data for m in qset]

    def create(self, validated_data):
        return QuizzLog.objects.create(**validated_data)




class LivegameListSerializer(serializers.ModelSerializer):
    opponant=serializers.SerializerMethodField()
    class Meta:
        model = QuizzLog
        fields =["room_code","opponant","sub_category"]

    def get_opponant(self,obj):
        print("\n>>>>>>>>>>>",list(obj.user.values()))
        return list(obj.user.values())[0]['username']










