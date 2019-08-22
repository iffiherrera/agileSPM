from django.db import models
from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User

# User field / Authentication 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

# Scrum Statement of Work model
class SOWScrum(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.TextField(unique=True)
    produced_by = models.CharField(max_length=128, blank=True)
    date_project = models.DateField(default=datetime.date.today)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    sprintLength = models.IntegerField(blank=False)
    sprint = models.IntegerField(blank=False)
    sprintPlan = models.TextField(blank=True)
    team = models.TextField(blank=True)
    done = models.TextField(blank=True)
    review = models.TextField(blank=True)
    milestones = models.DateField(default=datetime.date.today)
    milestone_description = models.CharField(max_length=128,blank=True) 
    delivery = models.DateField(default=datetime.date.today)
    invoice = models.DateField(default=datetime.date.today)
    invoice_info = models.CharField(max_length=128, blank=True)
    amount = models.FloatField(default=0,blank=False)
    firstName = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today)
    secondName = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)
    
    def save(self, *args, **kwargs):
        super(SOWScrum, self).save(*args, **kwargs)

# Kanban Statement of Work database fields
class SOWKanban(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.TextField(unique=True)
    produced_by = models.CharField(max_length=128, blank=True)
    date_project = models.DateField(default=datetime.date.today)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    plan = models.TextField(blank=True)
    columns = models.IntegerField(blank=True)
    column_labels = models.TextField(blank=True)
    wipLimit = models.IntegerField(default=1,blank=False)
    delivery = models.DateField(default=datetime.date.today)
    milestones = models.DateField(default=datetime.date.today)
    milestone_description = models.CharField(max_length=128,blank=True) 
    delivery = models.DateField(default=datetime.date.today)
    invoice = models.DateField(default=datetime.date.today)
    invoice_info = models.CharField(max_length=128, blank=True)
    amount = models.FloatField(default=0,blank=False)
    firstName = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today)
    secondName = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)


    def save(self, *args, **kwargs):
        super(SOWKanban, self).save(*args, **kwargs)


# Scrumban Statement of Work database fields
class SOWScrumban(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.TextField(unique=True)
    produced_by = models.CharField(max_length=128, blank=True)
    date_project = models.DateField(default=datetime.date.today)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    plan = models.TextField(blank=True)
    iterations = models.IntegerField(blank=True)
    team = models.TextField(blank=True)
    wipLimit = models.IntegerField(default=1,blank=False)
    review = models.TextField(blank=True)
    milestones = models.DateField(default=datetime.date.today)
    milestone_description = models.CharField(max_length=128,blank=True) 
    delivery = models.DateField(default=datetime.date.today)
    invoice = models.DateField(default=datetime.date.today)
    invoice_info = models.CharField(max_length=128, blank=True)
    amount = models.FloatField(default=0,blank=False)
    firstName = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today)
    secondName = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)

    def save(self, *args, **kwargs):
        super(SOWScrumban, self).save(*args, **kwargs)



