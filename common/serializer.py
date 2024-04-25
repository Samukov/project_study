# python object  ---> Json format
# JSON format ---> python object
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

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

class HeaderSettingsSerializer(serializers.Serializer):

    header_photo = MediaURLSerializer()
    about_us_text_title = serializers.CharField()
    about_us_text = serializers.CharField()
    short_text_left = serializers.CharField()
    main_title = serializers.CharField()
    left_all_users_title = serializers.CharField()
    left_all_users = serializers.IntegerField()
    center_all_users_title = serializers.CharField()
    center_all_users = serializers.IntegerField()
    right_all_users_title = serializers.CharField()
    right_all_users = serializers.IntegerField()

class FooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = '__all__'
        read_only_fields = [fields]