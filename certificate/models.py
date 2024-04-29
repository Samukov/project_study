from django.db import models

from django.contrib.auth.models import User
from course.models import Course


# class Certificate(models.Model):
#     created = models.DateTimeField(auto_now_add=True,
#                                    verbose_name='Created')
#     # expiration_date =
#
#     user = models.ForeignKey(to=User,
#                              on_delete=models.CASCADE,
#                              verbose_name='User',
#                              related_name='user_certificates')
#     course = models.ForeignKey(to=Course,
#                                on_delete=models.CASCADE,
#                                verbose_name='Course',
#                                related_name='course_certificates')
