# Generated by Django 3.0 on 2020-08-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20200811_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='core_value',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='core_value',
            field=models.ManyToManyField(to='about.CoreValue'),
        ),
    ]
