# Generated by Django 3.0 on 2020-08-11 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corevalue',
            name='status',
        ),
    ]
