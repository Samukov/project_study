from rest_framework import serializers
from faq.models import FAQCategory, FAQ


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ['question', 'answer']


class FAQCategorySerializer(serializers.ModelSerializer):


    questions = FAQSerializer(many=True, read_only=True)
    class Meta:
        model = FAQCategory
        fields = ['id', 'title', 'questions']


