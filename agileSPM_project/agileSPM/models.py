from django.db import models
from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User

# Scrum Statement of Work model
class SOWScrum(models.Model):
    title = models.TextField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    produced_by = models.CharField(max_length=128, blank=True)
    date_project = models.DateField(default=datetime.date.today, blank=True)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    sprintLength = models.IntegerField(blank=True)
    sprint = models.IntegerField(blank=True)
    team = models.TextField(blank=True)
    done = models.TextField(blank=True)
    review = models.TextField(blank=True)
    milestones = models.DateField(default=datetime.date.today, blank=True)
    milestone_description = models.CharField(max_length=128,blank=True) 
    delivery = models.DateField(default=datetime.date.today, blank=True)
    invoice = models.DateField(default=datetime.date.today, blank=True)
    invoice_info = models.CharField(max_length=128, blank=True)
    amount = models.TextField(blank=True)
    firstName = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today, blank=True)
    secondName = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today, blank=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today, blank=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SOWScrum, self).save(*args, **kwargs)

class MilestonesScrum(models.Model):
    scrum = models.ForeignKey(SOWScrum, on_delete=models.CASCADE, blank=True)
    milestones_scrum = models.DateField(default=datetime.date.today, blank=True)
    milestone_description_scrum = models.CharField(max_length=128,blank=True) 

    def __str__(self):
        return self.scrum

    def save(self, *args, **kwargs):
        super(MilestonesScrum, self).save(*args, **kwargs)


class InvoiceScrum(models.Model):
    scrum = models.ForeignKey(SOWScrum, on_delete=models.CASCADE, blank=True)
    invoice_scrum = models.DateField(default=datetime.date.today, blank=True)
    invoice_info_scrum = models.CharField(max_length=128, blank=True)
    amount_scrum = models.TextField(blank=True)

    def __str__(self):
        return self.scrum

    def save(self, *args, **kwargs):
        super(InvoiceScrum, self).save(*args, **kwargs)
    

# Kanban Statement of Work database fields
class SOWKanban(models.Model):
    
    title = models.TextField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    produced_by = models.CharField(max_length=128, blank=True)
    date_project = models.DateField(default=datetime.date.today, blank=True)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    plan = models.TextField(blank=True)
    columns = models.IntegerField(blank=True)
    column_labels = models.TextField(blank=True)
    wipLimit = models.IntegerField(default=1,blank=True)
    delivery = models.DateField(default=datetime.date.today, blank=True)
    invoice = models.DateField(default=datetime.date.today, blank=True)
    invoice_info = models.CharField(max_length=128, blank=True)
    amount = models.FloatField(default=0,blank=True)
    firstName = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today, blank=True)
    secondName = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today, blank=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today, blank=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SOWKanban, self).save(*args, **kwargs)

class InvoiceKanban(models.Model):
    kanban = models.ForeignKey(SOWKanban, on_delete=models.CASCADE, blank=True)
    invoice_scrum = models.DateField(default=datetime.date.today, blank=True)
    invoice_info_kanban = models.CharField(max_length=128, blank=True)
    amount_kanban = models.TextField(blank=True)

    def __str__(self):
        return self.kanban

    def save(self, *args, **kwargs):
        super(InvoiceKanban, self).save(*args, **kwargs)


# Scrumban Statement of Work database fields
class SOWScrumban(models.Model):
    title = models.TextField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    produced_by = models.CharField(max_length=128, blank=True)
    date_project = models.DateField(default=datetime.date.today, blank=True)
    intro = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    assumptions = models.TextField(blank=True)
    inScope = models.TextField(blank=True)
    outScope = models.TextField(blank=True)
    backlog = models.TextField(blank=True)
    plan = models.TextField(blank=True)
    iterations = models.IntegerField(blank=True)
    team = models.TextField(blank=True)
    wipLimit = models.IntegerField(default=1,blank=True)
    review = models.TextField(blank=True)
    milestones = models.DateField(default=datetime.date.today, blank=True)
    milestone_description = models.CharField(max_length=128,blank=True) 
    delivery = models.DateField(default=datetime.date.today, blank=True)
    invoice = models.DateField(default=datetime.date.today, blank=True)
    invoice_info = models.CharField(max_length=128, blank=True)
    amount = models.FloatField(default=0,blank=True)
    firstName = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today, blank=True)
    secondName = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today, blank=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SOWScrumban, self).save(*args, **kwargs)


class MilestonesScrumban(models.Model):
    scrumban = models.ForeignKey(SOWScrumban, on_delete=models.CASCADE, blank=True)
    milestones_scrumban = models.DateField(default=datetime.date.today, blank=True)
    milestone_description_scrumban = models.CharField(max_length=128,blank=True) 

    def __str__(self):
        return self.scrumban

    def save(self, *args, **kwargs):
        super(MilestonesScrumban, self).save(*args, **kwargs)

class InvoiceScrumban(models.Model):
    scrumban = models.ForeignKey(SOWScrumban, on_delete=models.CASCADE, blank=True)
    invoice_scrumban = models.DateField(default=datetime.date.today, blank=True)
    invoice_info_scrumban = models.CharField(max_length=128, blank=True)
    amount_scrumban = models.TextField(blank=True)

    def __str__(self):
        return self.scrumban

    def save(self, *args, **kwargs):
        super(InvoiceScrumban, self).save(*args, **kwargs)


