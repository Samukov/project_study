from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from faq.models import FAQCategory, FAQ
from faq.serializers import FAQCategorySerializer

class FAQCategoryList(APIView):
    """Представление для получения списка всех категорий FAQ."""

    def get(self, request):
        categories = FAQCategory.objects.all()  # Получаем все категории FAQ
        serializer = FAQCategorySerializer(categories, many=True)
        return Response(serializer.data)

class FAQCategoryDetail(APIView):
    """Представление для получения всех FAQ конкретной категории."""

    def get(self, request, category_id):
        try:
            category = FAQCategory.objects.get(pk=category_id)  # Получаем категорию FAQ по ID
        except FAQCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Если категория не найдена, возвращаем 404

        serializer = FAQCategorySerializer(category)
        return Response(serializer.data)
