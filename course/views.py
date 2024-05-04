from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

class CourseList(APIView):
    """Представление для получения списка всех курсов."""

    def get(self, request):
        courses = Course.objects.all()  # Получаем все курсы
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class CourseDetail(APIView):
    """Представление для получения детальной информации о курсе."""

    def get(self, request, course_id):
        try:
            course = Course.objects.get(pk=course_id)  # Получаем курс по ID
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Если курс не найден, возвращаем 404

        serializer = CourseSerializer(course)
        return Response(serializer.data)


class CourseLessons(APIView):
    """Представление для получения всех уроков курса."""

    def get(self, request, course_id):
        try:
            course = Course.objects.get(pk=course_id)  # Получаем курс по ID
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Если курс не найден, возвращаем 404

        lessons = course.modules.all().values('module_lessons__title', 'module_lessons__lessonmaterial__title')  # Получаем все уроки и связанные с ними материалы
        return Response(lessons)



