from django.urls import path

from faq.views import *


urlpatterns = [
    path('faq-categories/', FAQCategoryAPIView.as_view(), name='faq-categories'),
    path('faq-questions/category/<int:id>/', FAQListByCategory.as_view(), name='faq-by-category'),
]
