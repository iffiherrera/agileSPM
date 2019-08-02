from django.db import models
import datetime
from django.template.defaultfilters import slugify

# User database field

# User authentication 

# Statement of Work database fields
class SOW(models.Model):
    title = models.TextField(unique=True)
    produced_by = models.CharField(max_length=128, blank=True)
    date_project = models.DateField(default=datetime.date.today)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    milestones = models.DateField(default=datetime.date.today)
    milestone_description = models.CharField(max_length=128,blank=True) 
    delivery = models.DateField(default=datetime.date.today)
    invoice = models.DateField(default=datetime.date.today)
    invoice_info = models.CharField(max_length=128, blank=True)
    amount = models.FloatField(default=0,blank=False)
    firstName = models.TextField(blank=True)
    firstSignature = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today)
    secondName = models.TextField(blank=True)
    secondSignature = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SOW, self).save(*args, **kwargs)

#Scrum specific data fields, foreign key to SOW
class Scrum(models.Model):

    title = models.ForeignKey(SOW, on_delete=models.CASCADE)
    sprintLength = models.IntegerField(blank=False)
    sprint = models.IntegerField(blank=False)
    sprintPlan = models.TextField(blank=True)
    team = models.TextField(blank=True)
    done = models.TextField(blank=True)
    review = models.TextField(blank=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)

# Kanban specific data, Foreign Key to SOW
class Kanban(models.Model):

    title = models.ForeignKey(SOW,on_delete=models.CASCADE)
    plan = models.TextField(blank=True)
    columns = models.IntegerField(blank=True)
    column_labels = models.TextField(blank=True)
    wipLimit = models.IntegerField(default=1,blank=False)
    delivery = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)

# Scrumban specific data fields, Foreign Key to SOW
class Scrumban(models.Model):

    title = models.ForeignKey(SOW,on_delete=models.CASCADE)
    plan = models.TextField(blank=True)
    iterations = models.IntegerField(blank=True)
    team = models.TextField(blank=True)
    wipLimit = models.IntegerField(default=1,blank=False)
    review = models.TextField(blank=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)







