# Generated by Django 2.2.3 on 2019-08-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agileSPM', '0007_sow_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sow',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
