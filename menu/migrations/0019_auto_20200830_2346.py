# Generated by Django 3.0.5 on 2020-08-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_menuitems_childrenmenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='menu_category',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main Course', 'Main Course'), ('Course Meal', 'Course Meal'), ('Dessert', 'Dessert'), ('Drink', 'Drink')], max_length=100, null=True),
        ),
    ]