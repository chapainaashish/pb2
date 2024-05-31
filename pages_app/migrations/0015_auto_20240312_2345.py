# Generated by Django 3.2 on 2024-03-12 16:45

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('pages_app', '0014_auto_20240111_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='additional_content',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='content',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Header Content'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='content_on_list',
            field=tinymce.models.HTMLField(blank=True, verbose_name='List Content'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='logo_on_navbar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo_on_navbar', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='thumbnail',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL),
        ),
    ]
