# Generated by Django 3.0.8 on 2020-08-11 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200811_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='menu_category',
            new_name='menus',
        ),
    ]
