# Generated by Django 5.0.4 on 2024-05-04 04:56

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('duration', models.PositiveIntegerField(verbose_name='Duration')),
                ('card_desc', ckeditor.fields.RichTextField(verbose_name='card description')),
                ('course_director', models.CharField(max_length=120, verbose_name='course director')),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('expert', 'Expert')], max_length=120, verbose_name='level')),
                ('long_desc', ckeditor.fields.RichTextField(verbose_name='long_desc')),
                ('course_aim', ckeditor.fields.RichTextField(verbose_name='course_aim')),
                ('course_responsibilities', ckeditor.fields.RichTextField(verbose_name='course_responsibilities')),
                ('is_published', models.BooleanField(default=False, verbose_name='is_published')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='LessonMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(choices=[('video', 'Video'), ('document', 'Document'), ('presentation', 'presenatation')], max_length=120, verbose_name='Material Type')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Lesson Material',
                'verbose_name_plural': 'Lesson Materials',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='description')),
                ('order', models.PositiveIntegerField(verbose_name='module_order')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('order', models.PositiveIntegerField(verbose_name='order')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_lessons', to='course.module', verbose_name='Module')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
    ]
