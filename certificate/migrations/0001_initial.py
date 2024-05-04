# Generated by Django 5.0.4 on 2024-05-04 04:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_certificates', to='course.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_certificates', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
