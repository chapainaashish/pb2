# Generated by Django 3.2 on 2024-05-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0012_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='region',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='service',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='sp1',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='sp2',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='sp3',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='world',
            name='interests',
        ),
        migrations.AlterModelOptions(
            name='filter',
            options={'ordering': ('types', 'name')},
        ),
        migrations.AlterField(
            model_name='filter',
            name='types',
            field=models.CharField(choices=[('WORLD', 'World'), ('COUNTRY', 'Country'), ('REGION', 'Region'), ('CITY', 'City'), ('FACILITY', 'Inside'), ('SERVICE', 'Services'), ('RATING', 'Awards'), ('SP1', 'Cuisine'), ('SP2', 'Style'), ('SP3', 'Pricing')], max_length=20),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='SP1',
        ),
        migrations.DeleteModel(
            name='SP2',
        ),
        migrations.DeleteModel(
            name='SP3',
        ),
        migrations.DeleteModel(
            name='World',
        ),
    ]
