# Generated by Django 3.2 on 2022-09-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='wine_rg',
        ),
        migrations.AddField(
            model_name='country',
            name='location',
            field=models.ManyToManyField(blank=True, to='filters.CulinaryRegion'),
        ),
    ]
