from rest_framework.generics import ListAPIView

from multimedia.serializers import *

class MultimediaGalleryFilesAPIView(ListAPIView):
    queryset = MultimediaGalleryFile.objects.all()[:8]
    serializer_class = MultimediaGalleryFileSerializer

