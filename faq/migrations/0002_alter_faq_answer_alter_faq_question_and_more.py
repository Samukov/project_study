# Generated by Django 5.0.4 on 2024-05-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(default=1, verbose_name='Answer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='faqcategory',
            name='title',
            field=models.CharField(max_length=120, verbose_name='title'),
        ),
    ]
