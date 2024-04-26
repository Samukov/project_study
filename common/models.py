from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.utils import validate_phone_number
class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _('Image')
        VIDEO = 'video', _('Video')
    file = models.FileField(_("File"),
                            upload_to='only_medias/',
                            validators=[
                                FileExtensionValidator(
                                    allowed_extensions=[
                                        'jpg', 'jpeg', 'png', 'apng',
                                        'avif', 'gif', 'jfif', 'pjpeg',
                                        'pjp', 'svg', 'webp',
                                        'mp4', 'avi', 'mov', 'wmv',
                                        'mkv', 'flv', 'webm', 'avchd'
                                    ]
                                )
                            ])
    file_type = models.CharField(_("File type"),
                                 max_length=10,
                                 choices=FileType.choices)
    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")
    def __str__(self):
        return f"Id: {self.id}|Name: {self.file.name.split('/')[-1]}"
    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'apng',
                                                     'avif', 'gif', 'jfif', 'pjpeg',
                                                     'pjp', 'svg', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov', 'wmv',
                                                     'mkv', 'flv', 'webm', 'avchd']:
                raise ValidationError(_("Invalid Video File"))

class CommonSettings(models.Model):
    instagram = models.URLField(_("instagram"))
    facebook = models.URLField(_("facebook"))
    youtube = models.URLField(_("youtube"))
    telegram = models.URLField(_("telegram"))
    class Meta:
        verbose_name = _("Common Settings")
        verbose_name_plural = _("Common Settings")
    def __str__(self):
        return f"Id: {self.id}|Instagram: {self.instagram}|Facebook: {self.facebook}|Youtube: {self.youtube}|Telegram: {self.telegram}"

class HeaderSettings(models.Model):
    header_photo = models.ForeignKey(Media, models.CASCADE, verbose_name=_("Header photo"))
    about_us_text_title = models.CharField(_("About us title"), max_length=120)
    about_us_text = models.TextField(_("About us text"))
    short_text_left = models.TextField(_("Short text left"))
    main_title = models.CharField(_("title"), max_length=120)
    left_all_users_title = models.CharField(_("left all users title"), max_length=120)
    left_all_users = models.PositiveIntegerField()
    center_all_users_title = models.CharField(_("center all users title"), max_length=120)
    center_all_users = models.PositiveIntegerField()
    right_all_users_title = models.CharField(_("right all users title"), max_length=120)
    right_all_users = models.PositiveIntegerField()

    class Meta:
        verbose_name = _("Header Settings")
        verbose_name_plural = _("Header Settings")
    def __str__(self):
        return f"Id: {self.id}|About us text title: {self.about_us_text_title}|Title: {self.main_title}|"

class FooterSettings(models.Model):
    address = models.CharField(_("address"), max_length=120)
    phone_number = models.CharField(_("phone number"), max_length=20, validators=[validate_phone_number])
    email = models.EmailField(_("Email"))
    location = models.URLField(_("location"))
    class Meta:
        verbose_name = _("Footer Settings")
        verbose_name_plural = _("Footer Settings")
    def __str__(self):
        return f"Id: {self.id}|Address: {self.address}|Phone Number: {self.phone_number}|Email: {self.email}|Location: {self.location}"