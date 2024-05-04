# python object ---> JSON format
# JSON format ---> python object
# ----------------------------------------------------------------
from rest_framework import serializers
from common.models import *


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None

        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except Exception:
            return "http://testserver" + str(media.file.url)


class CommonSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonSettings
        fields = '__all__'
        read_only_fields = [fields]


class HeaderSettingsSerializer(serializers.ModelSerializer):
    header_photo = MediaURLSerializer()

    class Meta:
        model = HeaderSettings
        fields = '__all__'
        read_only_fields = [fields]


class FooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = '__all__'
        read_only_fields = [fields]
