from rest_framework import serializers
from .models import FAQQuestionCategory, FAQQuestion, FAQAnswer


class FAQAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQAnswer
        fields = ('answer',)


class FAQQuestionSerializer(serializers.ModelSerializer):
    answer = FAQAnswerSerializer()

    class Meta:
        model = FAQQuestion
        fields = ('question', 'answer')


class FAQQuestionCategorySerializer(serializers.ModelSerializer):
    questions = FAQQuestionSerializer(many=True)

    class Meta:
        model = FAQQuestionCategory
        fields = ('title', 'questions')
