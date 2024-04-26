from rest_framework import generics
from .models import FAQQuestionCategory
from .serializers import FAQQuestionCategorySerializer


class FAQCategoryList(generics.ListAPIView):
    queryset = FAQQuestionCategory.objects.all()
    serializer_class = FAQQuestionCategorySerializer


class FAQCategoryDetail(generics.RetrieveAPIView):
    queryset = FAQQuestionCategory.objects.all()
    serializer_class = FAQQuestionCategorySerializer
    lookup_field = 'id'
from django.shortcuts import render

# Create your views here.
