# Generated by Django 3.2 on 2023-07-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0023_interest_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ('geo_link',)},
        ),
        migrations.AddField(
            model_name='region',
            name='geo_link',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
    ]
