from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from common.utils import validate_phone_number


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', 'rasm'
        VIDEO = 'video', 'video'

    file = models.FileField("Fayl",
                            upload_to='only_medias/',
                            validators=[FileExtensionValidator(
                                allowed_extensions=[
                                    'jpg', 'jpeg', 'png', 'apng',
                                    'avif', 'gif', 'jfif', 'pjpeg',
                                    'pjp', 'svg', 'webp',
                                    'mp4', 'avi', 'mov', 'wmv',
                                    'mkv', 'flv', 'webm', 'avchd'
                                ]
                            )])
    file_type = models.CharField("Fayl turi",
                                 max_length=10,
                                 choices=FileType.choices)

    class Meta:
        verbose_name = "Media ma'lumot"
        verbose_name_plural = "Media ma'lumotlar"

    def __str__(self):
        return f"Id: {self.id}|Name: {self.file.name.split('/')[-1]}"

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError("Invalid File Type")
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'apng',
                                                     'avif', 'gif', 'jfif', 'pjpeg',
                                                     'pjp', 'svg', 'webp']:
                raise ValidationError("Invalid Image File")
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov', 'wmv',
                                                     'mkv', 'flv', 'webm', 'avchd']:
                raise ValidationError("Invalid Video File")


class CommonSettings(models.Model):
    instagram = models.URLField("instagram")
    facebook = models.URLField("facebook")
    youtube = models.URLField("youtube")
    telegram = models.URLField("telegram")

    class Meta:
        verbose_name = "Umumiy sozlama"
        verbose_name_plural = "Umumiy sozlamalar"

    def __str__(self):
        return f"Id: {self.id}|Instagram: {self.instagram}"


class HeaderSettings(models.Model):
    header_photo = models.ForeignKey(Media, models.CASCADE, verbose_name="Header photo")
    about_us_text_title = models.CharField("About us title", max_length=120)
    about_us_text = models.TextField("About us text")
    short_text_left = models.TextField("Short text left")

    main_title = models.CharField("title", max_length=120)

    left_all_users_title = models.CharField("left all users title", max_length=120)
    left_all_users = models.PositiveIntegerField()
    center_all_users_title = models.CharField("center all users title", max_length=120)
    center_all_users = models.PositiveIntegerField()
    right_all_users_title = models.CharField("right all users title", max_length=120)
    right_all_users = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Header Settings"
        verbose_name_plural = "Header Settings"

    def __str__(self):
        return f"Id: {self.id}|About us text title: {self.about_us_text_title}|Title: {self.main_title}|"


class FooterSettings(models.Model):
    address = models.CharField("address", max_length=120)
    phone_number = models.CharField("phone number", max_length=20,
                                    validators=[validate_phone_number])
    email = models.EmailField("Email")
    location = models.URLField("location")

    class Meta:
        verbose_name = "Footer Settings"
        verbose_name_plural = "Footer Settings"

    def __str__(self):
        return f"Id: {self.id}|Address: {self.address}|Phone Number: {self.phone_number}|Email: {self.email}|Location: {self.location}"
