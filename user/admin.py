from django.contrib import admin
from user.models import Regions
from user.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Regions)