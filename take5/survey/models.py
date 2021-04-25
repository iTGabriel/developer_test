from django.db import models

# Create your models here.
# from django.contrib.auth.models import User

class Survey(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=120)
    
class SurveyQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=50)
    
class SurveyQuestionAlternative(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    question_alternative = models.CharField(max_length=30)
   
class SurveyUserAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    survey_question_alternative = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)