from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course.views import CourseViewSet, ModuleViewSet, LessonViewSet, LessonMaterialViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'materials', LessonMaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]