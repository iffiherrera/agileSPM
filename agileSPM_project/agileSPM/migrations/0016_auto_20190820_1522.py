# Generated by Django 2.2.3 on 2019-08-20 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agileSPM', '0015_auto_20190820_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sowkanban',
            name='author',
        ),
        migrations.RemoveField(
            model_name='sowscrum',
            name='author',
        ),
        migrations.RemoveField(
            model_name='sowscrumban',
            name='author',
        ),
    ]
