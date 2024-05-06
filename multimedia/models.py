from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Media


class MultimediaGalleryFile(models.Model):
    file = models.ForeignKey(Media, on_delete=models.CASCADE,
                             verbose_name=_("File"))

    class Meta:
        verbose_name = _("Multimedia Gallery File")
        verbose_name_plural = _("Multimedia Gallery Files")

    def __str__(self):
        return f"Id: {self.id}|File: {self.file.file.name.split('/')[-1]}"
