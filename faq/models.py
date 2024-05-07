from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQCategory(models.Model):
    title = models.CharField(_('title'),
                             max_length=120)

    class Meta:
        verbose_name = _('FAQ Category')
        verbose_name_plural = _('FAQ Categories')

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.TextField(_('Question'))
    answer = models.TextField(_('Answer'))
    category = models.ForeignKey(to=FAQCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Category'),
                                 related_name='questions')

    class Meta:
        verbose_name = _('FAQ Question')
        verbose_name_plural = _('FAQ Questions')

    def __str__(self):
        return self.question

