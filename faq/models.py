from django.db import models
from django.utils.translation import gettext_lazy as _

class FAQQuestionCategory(models.Model):
    title = models.CharField(_('title'),
                             max_length=120)

    class Meta:
        verbose_name = _('FAQ Category')
        verbose_name_plural = _('FAQ Categories')

    def __str__(self):
        return self.title

class FAQQuestion(models.Model):
    question = models.TextField(_('Question'))
    category = models.ForeignKey(to=FAQQuestionCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Category'),
                                 related_name='questions')

    class Meta:
        verbose_name = _('FAQ Question')
        verbose_name_plural = _('FAQ Questions')

    def __str__(self):
        return self.question

class FAQAnswer(models.Model):
      answer = models.TextField(_('Answer'))
      question = models.OneToOneField(to=FAQQuestion,
                                      on_delete=models.CASCADE,
                                      verbose_name=_('Question'),
                                      related_name='answer')

      class Meta:
          verbose_name= _('FAQ Answer')
          verbose_name_plural = _('FAQ Answers')

      def __str__(self):
          return self.answer