from django.contrib import admin

from course.models import *

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(LessonMaterial)


