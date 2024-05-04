from rest_framework import serializers
from course.models import Module
from course.serializers.lesson import LessonSerializer

class ModuleSerializer(serializers.ModelSerializer):
    module_lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = '__all__'
