from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    total_score = models.IntegerField(null=True,default=0)

class UserTotalScore(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    score = models.IntegerField(default=0,null=True)

    def __str__(self):
          return "%s's profile" % self.user

    def create_user_score(sender, instance, created, **kwargs):
        if created:
            profile, created = UserTotalScore.objects.get_or_create(user=instance)

    post_save.connect(create_user_score, sender=CustomUser)


class QuizzLog(models.Model):
    room_code = models.CharField(max_length=20,null=True)
    user = models.ManyToManyField(CustomUser,through= 'UserQuizzScore')
    sub_category = models.CharField(max_length=200,null=True)
    winner = models.CharField(max_length=200,null=True)
    active_flag = models.BooleanField(default=True,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null = True)
    completed_at = models.DateTimeField(auto_now=True,null = True)

class UserQuizzScore(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    quizzlog = models.ForeignKey(QuizzLog,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

from django.contrib.auth.models import AbstractUser





class QuestionModel(models.Model):
    img_question = models.ImageField(upload_to="questions", blank=True, null=True)
    question = models.TextField(null=True)
    option1 = models.CharField(max_length=200,null=True)
    option2 = models.CharField(max_length=200,null=True)
    option3 = models.CharField(max_length=200,null=True)
    option4 = models.CharField(max_length=200,null=True)
    correct_answer = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,null=True)
    sub_category = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.question)


class QuestionUpload(models.Model):
    exel_file_upload = models.FileField(upload_to="question_exel")


class QuestionUploadForm(ModelForm):
    class Meta:
        model= QuestionUpload
        fields="__all__"


