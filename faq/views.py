from rest_framework.generics import ListAPIView, RetrieveAPIView

from faq.models import *
from faq.serializers import *


class FAQCategoryAPIView(ListAPIView):
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer


class FAQListByCategory(RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_field = "id"
