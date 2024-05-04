from django.urls import path
from .views import FinalTestQuestions, SubmitTestAnswers, TestResult

urlpatterns = [
    path('final-tests/<int:final_test_id>/questions/', FinalTestQuestions.as_view(), name='final-test-questions'),
    path('submit-test-answers/', SubmitTestAnswers.as_view(), name='submit-test-answers'),
    path('final-tests/<int:final_test_id>/result/', TestResult.as_view(), name='test-result'),
]
