# Generated by Django 2.2.3 on 2019-07-30 12:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agileSPM', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrum',
            old_name='wipLimit',
            new_name='sprintLength',
        ),
        migrations.AddField(
            model_name='scrum',
            name='done',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scrum',
            name='review',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scrum',
            name='sprint',
            field=models.IntegerField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four')], default=1),
        ),
        migrations.AddField(
            model_name='scrum',
            name='sprintBacklog1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scrum',
            name='sprintBacklog2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scrum',
            name='sprintBacklog3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scrum',
            name='sprintBacklog4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scrum',
            name='sprintPlan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sow',
            name='assumptions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='backlog',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='date_project',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='sow',
            name='deliverables',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='delivery',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='sow',
            name='firstName',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='firstSignature',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='inScope',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='intro',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='invoice',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='sow',
            name='milestones',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='sow',
            name='outScope',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='secondName',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='secondSignature',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sow',
            name='title',
            field=models.TextField(unique=True),
        ),
        migrations.CreateModel(
            name='Scrumban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iterations', models.IntegerField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four')], default=1)),
                ('it1', models.TextField(blank=True)),
                ('it2', models.TextField(blank=True)),
                ('it3', models.TextField(blank=True)),
                ('it4', models.TextField(blank=True)),
                ('team', models.TextField(blank=True)),
                ('wipLimit', models.IntegerField(default=1)),
                ('scrumban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agileSPM.SOW')),
            ],
        ),
        migrations.CreateModel(
            name='Kanban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columns', models.IntegerField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five'), ('6', 'six')], default=1)),
                ('column1', models.CharField(blank=True, max_length=128)),
                ('column2', models.CharField(blank=True, max_length=128)),
                ('column3', models.CharField(blank=True, max_length=128)),
                ('column4', models.CharField(blank=True, max_length=128)),
                ('column5', models.CharField(blank=True, max_length=128)),
                ('column6', models.CharField(blank=True, max_length=128)),
                ('wipLimit', models.IntegerField(default=1)),
                ('kanban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agileSPM.SOW')),
            ],
        ),
    ]