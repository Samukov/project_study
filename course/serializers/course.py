from rest_framework import serializers
from course.models import Course
from course.serializers.module import ModuleSerializer

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
