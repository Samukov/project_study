from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from faq.models import FAQCategory, FAQ
from faq.serializers import FAQCategorySerializer

class FAQCategoryList(APIView):


    def get(self, request):
        categories = FAQCategory.objects.all()
        serializer = FAQCategorySerializer(categories, many=True)
        return Response(serializer.data)

class FAQCategoryDetail(APIView):

    def get(self, request, category_id):
        try:
            category = FAQCategory.objects.get(pk=category_id)
        except FAQCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FAQCategorySerializer(category)
        return Response(serializer.data)
