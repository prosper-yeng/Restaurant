# Generated by Django 3.0 on 2020-08-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_remove_contactmessage_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='has_responded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='response',
            field=models.TextField(blank=True),
        ),
    ]
