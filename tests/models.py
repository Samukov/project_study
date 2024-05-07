from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from course.models import Course


class FinalTest(models.Model):
    course = models.OneToOneField(to=Course,
                                  on_delete=models.CASCADE,
                                  verbose_name=_("Course"),
                                  related_name='final_exam')
    title = models.CharField(_('title'),
                             max_length=120)
    minutes_to_solve = models.IntegerField(default=0, verbose_name="Минуты для решения")
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    question_count = models.IntegerField(_("Question Count"))

    class Meta:
        verbose_name = _('Final Test')
        verbose_name_plural = _('Final Tests')

    def __str__(self):
        return f"Course: {self.course.title}| Final Exam: {self.title}"


class TestQuestion(models.Model):
    question = RichTextField(_("Question"))
    final_test = models.ForeignKey(to=FinalTest,
                                   on_delete=models.CASCADE,
                                   verbose_name=_("Final Test"),
                                   related_name='test_questions')
    order = models.IntegerField(_("Order"))

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")

    def __str__(self):
        return f"Course: {self.final_test.course.title}| Order: {self.order}| Question: {self.question}"




class TestVariant(models.Model):
    answer = models.CharField(_('answer'),
                              max_length=120)
    correct = models.BooleanField(_('correct'), default=False)
    test_question = models.ForeignKey(to=TestQuestion,
                                      on_delete=models.CASCADE,
                                      verbose_name=_("Test Question"),
                                      related_name='test_variants')

    class Meta:
        verbose_name = _("Test Variant")
        verbose_name_plural = _("Test Variants")

    def __str__(self):
        return f"Question: {self.test_question.question}| Answer: {self.answer}| Correct: {self.correct}"


class FinalExamResult(models.Model):
    user = models.ForeignKey('user.CustomUser',
                             on_delete=models.CASCADE,
                             verbose_name=_("user"))
    final_test = models.ForeignKey(FinalTest,
                                   on_delete=models.CASCADE,
                                   verbose_name=_("final exam"))
    correct_results = models.IntegerField(default=0, verbose_name=_("result"))

    incorrect_results = models.IntegerField(default=0, verbose_name=_("result"))


    class Meta:
        verbose_name = _("Final Exam Result")
        verbose_name_plural = _("Final Exam Results")

    def __str__(self):
        return f"{self.user.first_name}"
