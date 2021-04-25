from rest_framework import viewsets
from survey import models

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = models.Survey.objects.all()

class SurveyQuestionViewSet(viewsets.ModelViewSet):
    queryset = models.SurveyQuestion.objects.all()

class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    queryset = models.SurveyQuestionAlternative.objects.prefetch_related('survey').all()

class SurveyUserAnswerViewSet(viewsets.ModelViewSet):
    queryset = models.SurveyUserAnswer.objects.prefetch_related('survey').all()