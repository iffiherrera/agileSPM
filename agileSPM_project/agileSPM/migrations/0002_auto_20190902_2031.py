# Generated by Django 2.2.3 on 2019-09-02 20:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agileSPM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sowkanban',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sowkanban',
            name='date_project',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowkanban',
            name='date_signature1',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowkanban',
            name='date_signature2',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowkanban',
            name='delivery',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowkanban',
            name='invoice',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowkanban',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.date.today, verbose_name='Last updated'),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='amount',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='date_project',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='date_signature1',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='date_signature2',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='delivery',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='invoice',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='milestones',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='sprint',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='sprintLength',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='sowscrum',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.date.today, verbose_name='Last updated'),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='date_project',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='date_signature1',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='date_signature2',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='delivery',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='invoice',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='milestones',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='sowscrumban',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.date.today, verbose_name='Last updated'),
        ),
        migrations.CreateModel(
            name='MilestonesScrumban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestones_scrumban', models.DateField(blank=True, default=datetime.date.today)),
                ('milestone_description_scrumban', models.CharField(blank=True, max_length=128)),
                ('scrumban', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agileSPM.SOWScrumban')),
            ],
        ),
        migrations.CreateModel(
            name='MilestonesScrum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestones_scrum', models.DateField(blank=True, default=datetime.date.today)),
                ('milestone_description_scrum', models.CharField(blank=True, max_length=128)),
                ('scrum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agileSPM.SOWScrum')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceScrum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_scrum', models.DateField(blank=True, default=datetime.date.today)),
                ('invoice_info_scrum', models.CharField(blank=True, max_length=128)),
                ('amount_scrum', models.TextField(blank=True)),
                ('scrum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agileSPM.SOWScrum')),
            ],
        ),
    ]