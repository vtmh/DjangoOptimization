# Generated by Django 3.0.6 on 2020-05-22 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_loginentry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginentry',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
