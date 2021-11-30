from django.db import models

class QuizzHistroy(models.Model):
    room_code = models.CharField(max_length=20,null=True)
    user_and_score = models.JSONField(encoder = None,null=True)
    winner = models.CharField(max_length=200,null=True)
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


