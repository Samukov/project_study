from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from common.models import Media


# username, first_name, last_name, email, password1, password2

class Regions(models.Model):
    name = models.CharField(max_length=120,
                            verbose_name=_('name'))

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    photo = models.ForeignKey(to=Media,
                              on_delete=models.CASCADE,
                              verbose_name=_("Photo"))
    age = models.PositiveIntegerField(_("Age"))
    gender = models.CharField(_("Gender"), max_length=10,
                              choices=GenderChoices.choices)
    phone_number = models.CharField(max_length=15)
    region = models.ForeignKey(to=Regions,
                               on_delete=models.CASCADE,
                               verbose_name=_("Region"))
    # Задаем related_name для полей groups и user_permissions
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True,
                                              related_name='custom_user_permissions')

