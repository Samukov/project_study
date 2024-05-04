from django.urls import path
from faq.views import FAQCategoryList, FAQCategoryDetail

urlpatterns = [
    path('categories/', FAQCategoryList.as_view(), name='faq-categories'),  # URL для списка категорий FAQ
    path('categories/<int:category_id>/', FAQCategoryDetail.as_view(), name='faq-category-detail'),  # URL для деталей категории FAQ
]
