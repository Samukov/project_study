from django.urls import path

from multimedia.views import *

urlpatterns = [
    path('multimedia_files/', MultimediaGalleryFilesAPIView.as_view(), name='multimedia_files')
]
