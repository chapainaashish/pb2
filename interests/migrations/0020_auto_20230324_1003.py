# Generated by Django 3.2 on 2023-03-24 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0019_alter_interest_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='web_text2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='interest',
            name='website2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]