from rest_framework import viewsets
from rest_framework.response import Response
from course.models import Lesson
from course.serializers.lesson import LessonSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
