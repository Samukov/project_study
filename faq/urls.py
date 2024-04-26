from django.urls import path

from faq.views import *


urlpatterns = [
    path('faq_categories/', FAQCategoryList.as_view(), name='faq_category_list'),
    path('faq_categories/<int:id>/', FAQCategoryDetail.as_view(), name='faq_category_detail'),
]
