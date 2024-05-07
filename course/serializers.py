from rest_framework import serializers
from .models import Course, Module, Lesson

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title']

class ModuleSerializer(serializers.ModelSerializer):

    module_lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['title', 'module_lessons']

class CourseSerializer(serializers.ModelSerializer):

    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['title', 'photo', 'duration', 'modules']
