from django.urls import path
from .views import CourseList, CourseDetail, CourseLessons

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),  # kurs spiskasi
    path('courses/<int:course_id>/', CourseDetail.as_view(), name='course-detail'),
    path('courses/<int:course_id>/lessons/', CourseLessons.as_view(), name='course-lessons'),  # URL для уроков курса
]
