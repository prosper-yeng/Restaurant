# Generated by Django 3.0.5 on 2020-08-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20200830_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='menu_desc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]