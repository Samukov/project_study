from django.urls import path

from common.views import *

urlpatterns = [
    path("common_settings/", CommonSettingsView.as_view(), name="common_settings"),
    path("header_settings/", HeaderSettingsView.as_view(), name="header_settings"),
    path("footer_settings/", FooterSettingsView.as_view(), name="footer_settings"),
]
