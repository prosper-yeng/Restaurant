# Generated by Django 3.0 on 2020-08-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_remove_aboutus_core_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='corevalue',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
