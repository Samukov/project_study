from rest_framework import serializers
from course.models import LessonMaterial

class LessonMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonMaterial
        fields = '__all__'

