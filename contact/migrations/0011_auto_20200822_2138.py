# Generated by Django 3.0.5 on 2020-08-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_contactmessage_has_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='has_message',
            field=models.BooleanField(default=True),
        ),
    ]