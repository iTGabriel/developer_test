from rest_framework import viewsets
from survey.api import serializers
from survey import models

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = models.Survey.objects.all()
    serializer_class = serializers.SurveySerializer

class SurveyQuestionViewSet(viewsets.ModelViewSet):
    queryset = models.SurveyQuestion.objects.all()
    serializer_class = serializers.SurveyQuestionSerializer

class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    queryset = models.SurveyQuestionAlternative.objects.prefetch_related('survey').all()
    serializer_class = serializers.SurveyQuestionAlternativeSerializer

class SurveyUserAnswerViewSet(viewsets.ModelViewSet):
    queryset = models.SurveyUserAnswer.objects.prefetch_related('survey').all()
    serializer_class = serializers.SurveyUserAnswerSerializer