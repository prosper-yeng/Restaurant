# Generated by Django 3.0.8 on 2020-08-12 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20200811_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spetials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('title', models.TextField(max_length=200, null=True)),
                ('tagline', models.TextField(max_length=200, null=True)),
                ('desc', models.TextField(max_length=200, null=True)),
                ('menuImage', models.FileField(upload_to='pics')),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Specials',
            },
        ),
    ]