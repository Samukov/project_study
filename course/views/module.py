from rest_framework import viewsets
from rest_framework.response import Response
from course.models import Module
from course.serializers.module import ModuleSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
