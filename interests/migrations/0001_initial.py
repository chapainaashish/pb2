# Generated by Django 3.2 on 2024-06-01 02:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import interests.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('text', tinymce.models.HTMLField(blank=True)),
                ('rating', models.FloatField(default=0)),
                ('google_map', models.TextField(blank=True)),
                ('info1_url', models.URLField(blank=True, verbose_name='LocationURL')),
                ('info1', models.CharField(blank=True, max_length=255, verbose_name='Location')),
                ('info2_url', models.URLField(blank=True, verbose_name='CuisineURL')),
                ('info2', models.CharField(blank=True, max_length=255, verbose_name='Cuisine')),
                ('info3_url', models.URLField(blank=True, verbose_name='PricingURL')),
                ('info3', models.CharField(blank=True, max_length=255, verbose_name='Pricing')),
                ('info4_url', models.URLField(blank=True, verbose_name='SeatingURL')),
                ('info4', models.CharField(blank=True, max_length=255, verbose_name='Seating')),
                ('info5_url', models.URLField(blank=True, verbose_name='ChefURL')),
                ('info5', models.CharField(blank=True, max_length=255, verbose_name='Chef')),
                ('long_info1', models.TextField(blank=True, verbose_name='Opening Hours')),
                ('cover', models.ImageField(blank=True, max_length=255, upload_to='img/%Y/%m/')),
                ('sidebar', models.TextField(blank=True)),
                ('ad_manager', models.TextField(blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('meta_keywords', models.TextField(blank=True)),
                ('carousel_title', models.CharField(blank=True, max_length=255)),
                ('top_slider', models.BooleanField(default=False)),
                ('cover_slider', models.BooleanField(default=False)),
                ('hide_rating', models.BooleanField(default=False)),
                ('display', models.BooleanField(default=False)),
                ('send_email', models.BooleanField(default=True)),
                ('display_list', models.BooleanField(default=True, verbose_name='Display Carousel')),
                ('display_billboard', models.BooleanField(default=True)),
                ('linkup_tags', models.TextField(blank=True)),
                ('username', models.CharField(blank=True, max_length=30)),
                ('email1', models.EmailField(blank=True, max_length=254)),
                ('email2', models.EmailField(blank=True, max_length=254)),
                ('address', models.TextField(blank=True)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('web_text', models.CharField(blank=True, max_length=255)),
                ('website2', models.CharField(blank=True, max_length=255, verbose_name='ReservationURL')),
                ('web_text2', models.CharField(blank=True, max_length=255, verbose_name='Reservation')),
                ('number', models.CharField(blank=True, max_length=20)),
                ('isvalidated', models.BooleanField(default=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('cover2', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL)),
                ('custom_overlay', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custom_overlay+', to=settings.FILER_IMAGE_MODEL)),
                ('list_carousel', models.ManyToManyField(blank=True, to='list.Category')),
                ('logo_on_navbar', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo_on_navbar+', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'Restaurant',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_link', models.CharField(blank=True, editable=False, max_length=255)),
                ('geo_filters', models.CharField(choices=[('WORLD', 'World'), ('COUNTRY', 'Country'), ('REGION', 'Region'), ('LOCAL', 'Local'), ('CITY', 'City'), ('NONE', 'None')], default='WORLD', max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('description_on_list', tinymce.models.HTMLField(blank=True)),
                ('sidebar', models.TextField(blank=True)),
                ('ad_manager', models.TextField(blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('meta_keywords', models.TextField(blank=True)),
                ('listing_title1', models.CharField(blank=True, max_length=255)),
                ('carousel_title', models.CharField(blank=True, max_length=255)),
                ('display_on_navbar', models.BooleanField(default=True)),
                ('display_list', models.BooleanField(default=True, verbose_name='Display Carousel')),
                ('display_billboard', models.BooleanField(default=True)),
                ('navbar_order', models.IntegerField(unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('list_carousel', models.ManyToManyField(blank=True, to='list.Category')),
                ('logo_on_navbar', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo_on_navbar+', to=settings.FILER_IMAGE_MODEL)),
                ('region_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interests.region')),
                ('thumbnail', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thumbnail+', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'ordering': ('geo_link',),
            },
        ),
        migrations.CreateModel(
            name='TopSliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL)),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interests.interest')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewAndRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('title', models.CharField(max_length=255)),
                ('review', models.TextField(validators=[interests.models.review_validator])),
                ('value', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('service', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('cleanliness', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('location', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('sustainability', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interests.interest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interests.region')),
                ('region_images', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='interest',
            name='region',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='interests.region'),
        ),
        migrations.AddField(
            model_name='interest',
            name='regions',
            field=models.ManyToManyField(blank=True, related_name='regions', to='interests.Region'),
        ),
        migrations.AddField(
            model_name='interest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CoverSliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL)),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interests.interest')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(validators=[interests.models.review_validator])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('rr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='interests.reviewandrating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
