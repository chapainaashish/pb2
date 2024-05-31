# Generated by Django 3.2 on 2022-09-15 18:30

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('interests', '0001_initial'),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('PAGE', 'Page'), ('FOOTER', 'Footer'), ('HOME_PAGE', 'Home Page'), ('SEARCH_PAGE', 'Search Page'), ('LIST', 'List'), ('WITHOUT_SIDEBAR', 'Without Sidebar')], max_length=20)),
                ('thumbnail', models.ImageField(blank=True, max_length=255, upload_to='thumbnail-page/')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Header Content')),
                ('additional_content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Main Content')),
                ('content_on_list', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='List Content')),
                ('sidebar', models.TextField(blank=True)),
                ('ad_manager', models.TextField(blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('meta_keywords', models.TextField(blank=True)),
                ('listing_title1', models.CharField(blank=True, max_length=255, verbose_name='Title Region List')),
                ('show_listing1', models.BooleanField(default=False, verbose_name='Display List Regions')),
                ('listing_title2', models.CharField(blank=True, max_length=255, verbose_name='Title Post List')),
                ('show_listing2', models.BooleanField(default=False, verbose_name='Display List Posts')),
                ('listing_title3', models.CharField(blank=True, max_length=255, verbose_name='Title Section 3')),
                ('show_listing3', models.BooleanField(default=False, verbose_name='Display List3')),
                ('carousel_title', models.CharField(blank=True, max_length=255, verbose_name='Title Carousel')),
                ('display_list', models.BooleanField(default=True, verbose_name='Display Carousel')),
                ('display_billboard', models.BooleanField(default=True, verbose_name='Display Billboards')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('category', models.ManyToManyField(blank=True, to='interests.Region', verbose_name='List Regions')),
                ('list_carousel', models.ManyToManyField(blank=True, related_name='_pages_app_contentpage_list_carousel_+', to='list.Category', verbose_name='List Carousel')),
                ('list_section', models.ManyToManyField(blank=True, related_name='_pages_app_contentpage_list_section_+', to='list.Category', verbose_name='List Posts')),
                ('thumbnail2', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True)),
                ('new_window', models.BooleanField(default=False)),
                ('order', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('script', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sidebar', models.TextField(blank=True)),
                ('ad_manager', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True)),
                ('order', models.IntegerField(unique=True)),
                ('page', models.ManyToManyField(blank=True, to='pages_app.ContentPage')),
                ('region', models.ManyToManyField(blank=True, to='interests.Region')),
            ],
        ),
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='page/')),
                ('image2', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages_app.contentpage')),
            ],
        ),
    ]
