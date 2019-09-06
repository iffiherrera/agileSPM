from django.db import models
from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User

## The models for the system with all relevant fields, utilises SQLite3 and is based on Django's ORM. ##

# Scrum Statement of Work model developed using the ER diagram presented in the project folder.
class SOWScrum(models.Model):
    title = models.TextField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    produced_by = models.CharField(max_length=128, null=True)
    date_project = models.DateField(default=datetime.date.today, null=True)
    intro = models.TextField(null=True)
    deliverables = models.TextField(null=True)
    assumptions = models.TextField(null=True)
    inScope = models.TextField(null=True)
    outScope = models.TextField(null=True)
    backlog = models.TextField(null=True)
    sprintLength = models.IntegerField(null=True)
    sprint = models.IntegerField(null=True)
    team = models.TextField(null=True)
    done = models.TextField(null=True)
    review = models.TextField(null=True)
    milestones = models.DateField(default=datetime.date.today, null=True)
    milestone_description = models.CharField(max_length=128,null=True) 
    delivery = models.DateField(default=datetime.date.today, null=True)
    invoice = models.DateField(default=datetime.date.today, null=True)
    invoice_info = models.CharField(max_length=128, null=True)
    amount = models.TextField(null=True)
    firstName = models.TextField(null=True)
    date_signature1 = models.DateField(default=datetime.date.today, null=True)
    secondName = models.TextField(null=True)
    date_signature2 = models.DateField(default=datetime.date.today, null=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today, null=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SOWScrum, self).save(*args, **kwargs)

# Additional fields for invoices & milestones commented out and waiting integration to the rest of the code

# class MilestonesScrum(models.Model):
#     scrum = models.ForeignKey(SOWScrum, on_delete=models.CASCADE, blank=True)
#     milestones_scrum = models.DateField(default=datetime.date.today, blank=True)
#     milestone_description_scrum = models.CharField(max_length=128,blank=True) 

#     def __str__(self):
#         return self.scrum

#     def save(self, *args, **kwargs):
#         super(MilestonesScrum, self).save(*args, **kwargs)


# class InvoiceScrum(models.Model):
#     scrum = models.ForeignKey(SOWScrum, on_delete=models.CASCADE, blank=True)
#     invoice_scrum = models.DateField(default=datetime.date.today, blank=True)
#     invoice_info_scrum = models.CharField(max_length=128, blank=True)
#     amount_scrum = models.TextField(blank=True)

#     def __str__(self):
#         return self.scrum

#     def save(self, *args, **kwargs):
#         super(InvoiceScrum, self).save(*args, **kwargs)
    

## Kanban Statement of Work model developed using the ER diagram presented in the project folder.
class SOWKanban(models.Model):
    
    title = models.TextField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    produced_by = models.CharField(max_length=128, null=True)
    date_project = models.DateField(default=datetime.date.today, null=True)
    intro = models.TextField(null=True)
    deliverables = models.TextField(null=True)
    assumptions = models.TextField(null=True)
    inScope = models.TextField(null=True)
    outScope = models.TextField(null=True)
    backlog = models.TextField(null=True)
    plan = models.TextField(null=True)
    columns = models.IntegerField(null=True)
    column_labels = models.TextField(null=True)
    wipLimit = models.IntegerField(default=1,null=True)
    delivery = models.DateField(default=datetime.date.today, null=True)
    invoice = models.DateField(default=datetime.date.today, null=True)
    invoice_info = models.CharField(max_length=128, null=True)
    amount = models.FloatField(default=0,null=True)
    firstName = models.TextField(null=True)
    date_signature1 = models.DateField(default=datetime.date.today, null=True)
    secondName = models.TextField(null=True)
    date_signature2 = models.DateField(default=datetime.date.today, null=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today, null=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SOWKanban, self).save(*args, **kwargs)

# Additional fields for invoices commented out and waiting integration to the rest of the code

# class InvoiceKanban(models.Model):
#     kanban = models.ForeignKey(SOWKanban, on_delete=models.CASCADE, blank=True)
#     invoice_scrum = models.DateField(default=datetime.date.today, blank=True)
#     invoice_info_kanban = models.CharField(max_length=128, blank=True)
#     amount_kanban = models.TextField(blank=True)

#     def __str__(self):
#         return self.kanban

#     def save(self, *args, **kwargs):
#         super(InvoiceKanban, self).save(*args, **kwargs)


# Scrumban Statement of Work model developed using the ER diagram presented in the project folder.
class SOWScrumban(models.Model):
    title = models.TextField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    produced_by = models.CharField(max_length=128, null=True)
    date_project = models.DateField(default=datetime.date.today, null=True)
    intro = models.TextField(null=True)
    deliverables = models.TextField(null=True)
    assumptions = models.TextField(null=True)
    inScope = models.TextField(null=True)
    outScope = models.TextField(null=True)
    backlog = models.TextField(null=True)
    plan = models.TextField(null=True)
    iterations = models.IntegerField(null=True)
    team = models.TextField(null=True)
    wipLimit = models.IntegerField(default=1,null=True)
    review = models.TextField(null=True)
    milestones = models.DateField(default=datetime.date.today, null=True)
    milestone_description = models.CharField(max_length=128,null=True) 
    delivery = models.DateField(default=datetime.date.today, null=True)
    invoice = models.DateField(default=datetime.date.today, null=True)
    invoice_info = models.CharField(max_length=128, null=True)
    amount = models.FloatField(default=0,null=True)
    firstName = models.TextField(null=True)
    date_signature1 = models.DateField(default=datetime.date.today, null=True)
    secondName = models.TextField(null=True)
    date_signature2 = models.DateField(default=datetime.date.today, null=True)
    updated = models.DateTimeField('Last updated', default=datetime.date.today, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SOWScrumban, self).save(*args, **kwargs)

# Additional fields for invoices & milestones commented out and waiting integration to the rest of the code

# class MilestonesScrumban(models.Model):
#     scrumban = models.ForeignKey(SOWScrumban, on_delete=models.CASCADE, blank=True)
#     milestones_scrumban = models.DateField(default=datetime.date.today, blank=True)
#     milestone_description_scrumban = models.CharField(max_length=128,blank=True) 

#     def __str__(self):
#         return self.scrumban

#     def save(self, *args, **kwargs):
#         super(MilestonesScrumban, self).save(*args, **kwargs)

# class InvoiceScrumban(models.Model):
#     scrumban = models.ForeignKey(SOWScrumban, on_delete=models.CASCADE, blank=True)
#     invoice_scrumban = models.DateField(default=datetime.date.today, blank=True)
#     invoice_info_scrumban = models.CharField(max_length=128, blank=True)
#     amount_scrumban = models.TextField(blank=True)

#     def __str__(self):
#         return self.scrumban

#     def save(self, *args, **kwargs):
#         super(InvoiceScrumban, self).save(*args, **kwargs)


