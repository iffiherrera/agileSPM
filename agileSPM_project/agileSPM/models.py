from django.db import models
import datetime

#Statement of Work database fields
class SOW(models.Model):
    title = models.TextField(unique=True)
    produced_by = models.CharField(max_length=128, blank=True)
    updated = models.DateTimeField('Last updated')
    date_project = models.DateField(default=datetime.date.today)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    milestones = models.DateField(default=datetime.date.today)
    delivery = models.DateField(default=datetime.date.today)
    invoice = models.DateField(default=datetime.date.today)
    amount = models.FloatField(default=0,blank=False)
    firstName = models.TextField(blank=True)
    firstSignature = models.TextField(blank=True)
    secondName = models.TextField(blank=True)
    secondSignature = models.TextField(blank=True)

#Scrum specific data fields, foreign key to SOW
class Scrum(models.Model):
    SPRINT_NUMBER = ( 
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
    )
    scrum = models.ForeignKey(SOW, on_delete=models.CASCADE)
    sprintLength = models.IntegerField(blank=False)
    sprint = models.IntegerField(default=1,choices=SPRINT_NUMBER)
    sprintBacklog1 = models.TextField(blank=True)
    sprintBacklog2 = models.TextField(blank=True)
    sprintBacklog3 = models.TextField(blank=True)
    sprintBacklog4 = models.TextField(blank=True)
    sprintPlan = models.TextField(blank=True)
    team = models.TextField(blank=True)
    done = models.TextField(blank=True)
    review = models.TextField(blank=True)

# Kanban specific data, Foreign Key to SOW
class Kanban(models.Model):
    # Set a column amount.
    WORKFLOW_COLUMNS = (
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
        ('5', 'five'),
        ('6', 'six'),
    )
    kanban = models.ForeignKey(SOW,on_delete=models.CASCADE)
    columns = models.IntegerField(default=1,choices=WORKFLOW_COLUMNS)
    column1 = models.CharField(max_length=128, blank=True)
    column2 = models.CharField(max_length=128, blank=True)
    column3 = models.CharField(max_length=128, blank=True)
    column4 = models.CharField(max_length=128, blank=True)
    column5 = models.CharField(max_length=128, blank=True)
    column6 = models.CharField(max_length=128, blank=True)
    wipLimit = models.IntegerField(default=1,blank=False)

# Scrumban specific data fields, Foreign Key to SOW
class Scrumban(models.Model):
     # Set a column amount.
    ITERATIONS = (
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
    )
    scrumban = models.ForeignKey(SOW,on_delete=models.CASCADE)
    iterations = models.IntegerField(default=1,choices=ITERATIONS)
    it1 = models.TextField(blank=True)
    it2 = models.TextField(blank=True)
    it3 = models.TextField(blank=True)
    it4 = models.TextField(blank=True)
    team = models.TextField(blank=True)
    wipLimit = models.IntegerField(default=1,blank=False)






