from rest_framework import viewsets
from rest_framework.response import Response
from course.models import LessonMaterial
from course.serializers.lesson_material import LessonMaterialSerializer

class LessonMaterialViewSet(viewsets.ModelViewSet):
    queryset = LessonMaterial.objects.all()
    serializer_class = LessonMaterialSerializer
