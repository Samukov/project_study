from rest_framework import serializers
from course.models import Lesson
from course.serializers.lesson_material import LessonMaterialSerializer

class LessonSerializer(serializers.ModelSerializer):
    lesson_materials = LessonMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

