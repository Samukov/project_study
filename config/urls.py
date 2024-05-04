from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.conf import settings
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Study Project API",
        default_version="v1",
        description="API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # API urls
    path("common/api/", include("common.urls")),
    path("faq/api/", include("faq.urls")),
    path("multimedia/api/", include("multimedia.urls")),
    path("course/api/", include("course.urls")),
    path("certificate/api/", include("multimedia.urls")),
    path("tests/api/", include("multimedia.urls")),
    path("user/api/", include("multimedia.urls")),
    path("statistika/api/", include("multimedia.urls")),
	re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
