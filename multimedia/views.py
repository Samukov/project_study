from rest_framework.generics import ListAPIView

from multimedia.models import *
from multimedia.serializers import *


class MultimediaGalleryFilesAPIView(ListAPIView):
    queryset = MultimediaGalleryFile.objects.all()
    serializer_class = MultimediaGalleryFileSerializer

    def get_queryset(self):
        return MultimediaGalleryFile.objects.filter(file__isnull=False)
