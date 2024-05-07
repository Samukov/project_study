from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tests.models import *
from .serializers import TestQuestionSerializer


class FinalTestQuestions(APIView):

    def get(self, request, final_test_id):
        try:
            final_test = FinalTest.objects.get(pk=final_test_id)  # Получаем финальный тест по ID
        except FinalTest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Если тест не найден, возвращаем 404

        questions = final_test.test_questions.all()  # Получаем все вопросы для данного теста
        serializer = TestQuestionSerializer(questions, many=True)
        return Response(serializer.data)



class SubmitTestAnswers(APIView):

    def post(self, request):
        data = request.data
        # Обработка данных, сохранение ответов в базу данных
        return Response(status=status.HTTP_200_OK)  # Возвращаем успешный статус


class TestResult(APIView):

    def get(self, request, final_test_id):
        try:
            final_test = FinalTest.objects.get(pk=final_test_id)
        except FinalTest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            final_exam_result = FinalExamResult.objects.get(final_test=final_test)
        except FinalExamResult.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        total_questions = final_test.question_count
        correct_results = final_exam_result.correct_results
        incorrect_results = final_exam_result.incorrect_results

        if total_questions > 0:
            percentage_correct = (correct_results / total_questions) * 100
        else:
            percentage_correct = 0

        data = {
            'total_questions': total_questions,
            'correct_answers': correct_results,
            'incorrect_answers': incorrect_results,
            'percentage_correct': percentage_correct
        }

        return Response(data)
