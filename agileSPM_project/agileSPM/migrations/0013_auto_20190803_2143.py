# Generated by Django 2.2.3 on 2019-08-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agileSPM', '0012_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
