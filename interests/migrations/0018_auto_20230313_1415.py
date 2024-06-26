# Generated by Django 3.2 on 2023-03-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0017_rename_opening_hours_interest_long_info1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='info1',
            field=models.CharField(blank=True, max_length=255, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info1_url',
            field=models.URLField(blank=True, verbose_name='LocationURL'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Cuisine'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info2_url',
            field=models.URLField(blank=True, verbose_name='CuisineURL'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info3',
            field=models.CharField(blank=True, max_length=255, verbose_name='Pricing'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info3_url',
            field=models.URLField(blank=True, verbose_name='PricingURL'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info4',
            field=models.CharField(blank=True, max_length=255, verbose_name='Seating'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info4_url',
            field=models.URLField(blank=True, verbose_name='SeatingURL'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info5',
            field=models.CharField(blank=True, max_length=255, verbose_name='Chef'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='info5_url',
            field=models.URLField(blank=True, verbose_name='ChefURL'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='long_info1',
            field=models.TextField(blank=True, verbose_name='Opening Hours'),
        ),
    ]
