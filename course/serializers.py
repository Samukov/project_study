from rest_framework import serializers
from .models import Course, Module, Lesson

class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Lesson."""

    class Meta:
        model = Lesson
        fields = ['title']

class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Module, включая связанные уроки."""

    module_lessons = LessonSerializer(many=True, read_only=True)  # Сериализатор для связанных уроков

    class Meta:
        model = Module
        fields = ['title', 'module_lessons']

class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Course, включая связанные модули."""

    modules = ModuleSerializer(many=True, read_only=True)  # Сериализатор для связанных модулей

    class Meta:
        model = Course
        fields = ['title', 'photo', 'duration', 'modules']
