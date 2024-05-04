from rest_framework import viewsets
from rest_framework.response import Response
from course.models import Course
from course.serializers.course import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
