from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # API urls
    path('common/api/', include('common.urls')),
    path('faq/api/', include('faq.urls')),
    path('multimedia/api/', include('multimedia.urls')),
    path('course/api/', include('course.urls')),
    path('certificate/api/', include('certificate.urls')),
    path('tests/api/', include('tests.urls')),
    path('user/api/', include('user.urls')),
    path('statistika/api/', include('statistika.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
