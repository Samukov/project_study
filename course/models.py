from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from common.models import Media
from django.contrib.auth.models import User

class Course(models.Model):
    class LevelChoices(models.TextChoices):
        BEGINNER = 'beginner', _('Beginner')
        INTERMEDIATE = 'intermediate', _('Intermediate')
        ADVANCED = 'advanced', _('Advanced')
        EXPERT = 'expert', _('Expert')

    title = models.CharField(max_length=120)
    photo = models.ForeignKey(Media,
                              on_delete=models.CASCADE,
                              verbose_name=_("Photo"))
    duration = models.PositiveIntegerField(_('Duration'))
    card_desc = RichTextField(_('card description'))
    course_director = models.CharField(_('course director'),
                                       max_length=120)
    level = models.CharField(_('level'),
                             max_length=120,
                             choices=LevelChoices.choices)

    long_desc = RichTextField(_('long_desc'))
    course_aim = RichTextField(_('course_aim'))
    course_responsibilities = RichTextField(_('course_responsibilities'))

    is_published = models.BooleanField(_('is_published'), default=False)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name=_("Course"),
                               related_name='modules')
    title = models.CharField(_('title'),
                             max_length=120)
    description = RichTextField(_('description'))
    # lessons_count = models.PositiveIntegerField(_('lessons_count'))
    order = models.PositiveIntegerField(_('module_order'))
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')

    def __str__(self):
        return f"Course:{self.course.title}| Module:{self.title}"

class Lesson(models.Model):
    title = models.CharField(_('title'),
                             max_length=120)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE,
                               verbose_name=_("Module"),
                               null=True, blank=True,
                               related_name='module_lessons')
    order = models.PositiveIntegerField(_("order"))

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return f"Course: {self.module.course.title}| Module:{self.module.title}| Lesson:{self.title}"

class LessonMaterial(models.Model):
    class MaterialType(models.TextChoices):
        VIDEO = 'video', _('Video')
        DOCUMENT = 'document', _('Document')
        PRESENTATION = 'presentation', _('presenatation')

    material_type = models.CharField(_('Material Type'),
                                     max_length=120,
                                     choices=MaterialType.choices)
    title = models.CharField(_('title'),
                             max_length=120)
    file = models.ForeignKey(Media,
                             on_delete=models.CASCADE,
                             verbose_name=_("File"))
    class Meta:
        verbose_name = _('Lesson Material')
        verbose_name_plural = _('Lesson Materials')

    def __str__(self):
        return f"Lesson:{self.lesson.title}| Material:{self.title}"
