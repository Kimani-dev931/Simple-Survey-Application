from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Question, SurveyResponse, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['G_value', 'PS_value']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class SurveyResponseSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(default=None)

    class Meta:
        model = SurveyResponse
        fields = '__all__'
        extra_kwargs = {'question': {'required': False}}
