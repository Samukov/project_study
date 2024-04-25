
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),


    #api url

    path('common/', include('common.urls')),
    path('faq/', include('faq.urls')),
    path('main_platform/', include('main_platform.urls')),
    path('multimedia/', include('multimedia.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
