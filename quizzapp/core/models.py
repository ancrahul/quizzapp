from django.db import models
from django.forms import ModelForm


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


class QuestionUpload(models.Model):
    exel_file_upload = models.FileField(upload_to="question_exel")


class QuestionUploadForm(ModelForm):
    class Meta:
        model= QuestionUpload
        fields="__all__"


