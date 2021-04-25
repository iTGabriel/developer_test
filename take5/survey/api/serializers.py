from rest_framework import serializers

from survey import models

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Survey
        fields = '__all__'

class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyQuestion
        fields = '__all__'

class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyQuestionAlternative
        fields = '__all__'

class SurveyUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyUserAnswer
        fields = '__all__'