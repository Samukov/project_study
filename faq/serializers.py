from rest_framework import serializers
from faq.models import FAQCategory, FAQ


class FAQSerializer(serializers.ModelSerializer):
    """Сериализатор для модели FAQ."""

    class Meta:
        model = FAQ
        fields = ['question', 'answer']


class FAQCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели FAQCategory."""

    questions = FAQSerializer(many=True, read_only=True)  # Сериализатор для связанных вопросов FAQ

    class Meta:
        model = FAQCategory
        fields = ['id', 'title', 'questions']


