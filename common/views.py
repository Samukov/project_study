from rest_framework.generics import RetrieveAPIView
from common.serializers import *
from common.models import *

class CommonSettingsView(RetrieveAPIView):
    serializers_class = CommonSettingsSerializer

    queryset = CommonSettings.objects.all()
    serializers_class = CommonSettingsSerializer

    def get_object(self):
        return CommonSettings.objects.first()
class HeaderSettingsView(RetrieveAPIView):

      queryset = HeaderSettings.objects.all()
      serializer_class = HeaderSettingsSerializer

      def get_object(self):
          return HeaderSettings.objects.first()

class FooterSettingsView(RetrieveAPIView):
      queryset = FooterSettings.objects.all()
      serializer_class = FooterSettingsSerializer

      def get_object(self):
          return FooterSettings.objects.first()

