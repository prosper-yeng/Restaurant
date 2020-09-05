# Generated by Django 3.0.5 on 2020-08-30 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20200830_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('status', models.BooleanField()),
                ('MenuSubCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.MenuCategory')),
            ],
            options={
                'verbose_name_plural': 'Menu Category Type',
            },
        ),
        migrations.RemoveField(
            model_name='menuitems',
            name='MenuCategoryType',
        ),
        migrations.RemoveField(
            model_name='menuitems',
            name='menuCategory',
        ),
        migrations.DeleteModel(
            name='MenuCategoryType',
        ),
        migrations.AddField(
            model_name='menuitems',
            name='menuSubCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.MenuSubCategory'),
        ),
    ]
