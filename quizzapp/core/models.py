from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserTotalScore(models.Model):  
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)  
    score = models.IntegerField(default=0)

    def __str__(self):  
          return "%s's profile" % self.user  

    def create_user_score(sender, instance, created, **kwargs):  
        if created:  
            UserTotalScore.objects.get_or_create(user=instance)  

    post_save.connect(create_user_score, sender=User, weak=False,dispatch_uid='models.create_user_score') 

    

class QuizzLog(models.Model):
    room_code = models.CharField(max_length=20,null=True)
    user = models.ManyToManyField(User,through= 'UserQuizzScore')
    sub_category = models.CharField(max_length=200,null=True)
    winner = models.CharField(max_length=200,null=True)
    active_flag = models.BooleanField(default=True,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null = True)
    completed_at = models.DateTimeField(auto_now=True,null = True)

class UserQuizzScore(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quizzlog = models.ForeignKey(QuizzLog,on_delete=models.CASCADE)
    score = models.IntegerField(null = True,default=0)


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
        return self.question

