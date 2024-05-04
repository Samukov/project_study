from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from common.models import Media


# username, first_name, last_name, email, password1, password2


class Regions(models.Model):
    name = models.CharField(max_length=120, verbose_name=_("name"))

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name
