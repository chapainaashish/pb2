# Generated by Django 3.2 on 2023-03-13 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0008_auto_20230213_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Award', 'verbose_name_plural': 'Award'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Service'},
        ),
        migrations.AlterModelOptions(
            name='world',
            options={'verbose_name': 'World', 'verbose_name_plural': 'World'},
        ),
    ]
