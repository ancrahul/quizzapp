from .models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields="__all__"
        # fields=["id","img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]







class LoginTokenPairSerializer(TokenObtainPairSerializer):
    ### Inserting Addition of user info into token  ####
    @classmethod
    def get_token(cls, user):
        token = super(LoginTokenPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['score'] = user.total_score
        return token



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




class QuestionCategorySerializer(serializers.Serializer):
    category = serializers.CharField()

class QuestionSubCategorySerializer(serializers.Serializer):
    sub_category = serializers.CharField()
        fields=["id","img_question","question","option1","option2","option3","option4","correct_answer","category","sub_category"]


class JoinOrCreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizzLog
        fields = ["id","room_code","user","sub_category","winner","active_flag","created_at","started_at","completed_at"]