# Generated by Django 3.0.5 on 2020-09-07 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200823_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_active',
        ),
        migrations.AddField(
            model_name='booking',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_time',
            field=models.TimeField(default='9:00 am'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='has_responded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='msg',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='msgemail',
            field=models.EmailField(default='hepeps3@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='response',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='your_name',
            field=models.CharField(default='john', max_length=100),
            preserve_default=False,
        ),
    ]
