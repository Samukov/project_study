from django.urls import path

from multimedia.views import *

urlpatterns = [
    path('files/', MultimediaGalleryFilesAPIView.as_view(), name='multimedia_files')
]
