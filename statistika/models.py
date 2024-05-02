from django.db import models
from django.utils.translation import gettext_lazy as _


class StatistikaCategory(models.Model):
    title = models.CharField(_('title'),
                             max_length=120)

    class Meta:
        verbose_name =_('Static Category')
        verbose_name_plural =_('Static Categories')

    def __str__(self):
        return self.title


class Statistika(models.Model):
    title = models.CharField(_('title')),
    regions = models.TextField(_('Region')),
    number = models.IntegerField(_('number_user'))
    minutes_to_solve = models.IntegerField(default=0, verbose_name="Yangilanish vaqti")
    category=models.ForeignKey(to=StatistikaCategory,
                               on_delete=models.CASCADE,
                               verbose_name='Static Category',
                               verbose_name_plural='Static Category')

    class Meta:
        verbose_name = _('Statistika')
        verbose_name_plural = _('Statistika')

    def __str__(self):
        return self.title



