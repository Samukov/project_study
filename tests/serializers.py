from rest_framework import serializers
from tests.models import FinalTest, TestQuestion, TestVariant, FinalExamResult

class TestVariantSerializer(serializers.ModelSerializer):
    """Сериализатор для модели TestVariant."""

    class Meta:
        model = TestVariant
        fields = ['answer', 'correct']

class TestQuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели TestQuestion, включая связанные варианты ответов."""

    test_variants = TestVariantSerializer(many=True, read_only=True)  # Сериализатор для связанных вариантов ответов

    class Meta:
        model = TestQuestion
        fields = ['question', 'test_variants']

class FinalTestSerializer(serializers.ModelSerializer):
    """Сериализатор для модели FinalTest, включая связанные вопросы теста."""

    test_questions = TestQuestionSerializer(many=True, read_only=True)  # Сериализатор для связанных вопросов теста

    class Meta:
        model = FinalTest
        fields = ['title', 'minutes_to_solve', 'test_questions']
