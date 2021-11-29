from django.db import models
# Create your models here.
# class QuestionModel(models.Model):
    
#     img_question = models.ImageField(upload_to='Question',blank=True, null=True)
#     question = models.TextField(null=True)
#     option1 = models.CharField(max_length=200,null=True)
#     option2 = models.CharField(max_length=200,null=True)
#     option3 = models.CharField(max_length=200,null=True)
#     option4 = models.CharField(max_length=200,null=True)
#     correct_answer = models.CharField(max_length=200,null=True)
#     category = models.CharField(max_length=200,null=True)
#     sub_category = models.CharField(max_length=200,null=True)
    
#     def __str__(self):
#         return self.question

class QuizzHistroy(models.Model):
    # user1,user1 score,user2,user2 score,winner,looser,created at,started at,completed at.
    user1 = models.ForeignKey()
    user1_score = models.IntegerField()
    user2 = models.ForeignKey()
    user2_score = models.IntegerField()
    winner = models.CharField(max_length=200,null=True)
    looser = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(auto_now=True,null = True)
    completed_at = models.DateTimeField(auto_now=True,null = True)


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


