from rest_framework import serializers

from multimedia.models import *
from common.serializers import MediaURLSerializer


class MultimediaGalleryFileSerializer(serializers.ModelSerializer):
    file = MediaURLSerializer()

    class Meta:
        model = MultimediaGalleryFile
        fields = ('id', 'file',)
        read_only_fields = [fields]

