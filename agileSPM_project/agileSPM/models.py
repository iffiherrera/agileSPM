from django.db import models
from django.forms import ModelForm
import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# User field / Authentication 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    
    def __str__(self):
        return self.user.username


# Scrum Statement of Work model
class SOWScrum(models.Model):
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
    firstSignature = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today)
    secondName = models.TextField(blank=True)
    secondSignature = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SOWScrum, self).save(*args, **kwargs)

## Scrum Model forms set for the forms.py user input ##
class CoverScrum1(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['title','produced_by','date_project','updated','slug',]

class IntroScrum2(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['intro','updated']

class ObjectivesScrum3(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['deliverables','assumptions','updated',]

class ScopeScrum4(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['inScope','outScope','updated',]

class BacklogScrum5(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['backlog','updated',]

class ScrumForm6(ModelForm):
    class Meta: 
        model = SOWScrum
        fields = ['sprintPlan','sprintLength','sprint','team','done','review','updated',]

class MilestonesScrum7(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['milestones','milestone_description','delivery','updated',]

class CostScrum8(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['invoice','invoice_info','amount','updated']

class AcceptanceScrum9(ModelForm):
    class Meta:
        model = SOWScrum
        fields = ['firstName','firstSignature','date_signature1',
                    'secondName','secondSignature','date_signature2','updated',]


# Kanban Statement of Work database fields
class SOWKanban(models.Model):
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
    firstSignature = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today)
    secondName = models.TextField(blank=True)
    secondSignature = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SOWKanban, self).save(*args, **kwargs)

## Kanban Model forms set for the forms.py user input ##
class CoverKanban1(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['title','produced_by','date_project','updated','slug',]

class IntroKanban2(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['intro','updated']

class ObjectivesKanban3(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['deliverables','assumptions','updated',]

class ScopeKanban4(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['inScope','outScope','updated',]

class BacklogKanban5(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['backlog','updated',]

class KanbanForm6(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['plan','columns','column_labels','wipLimit','delivery','updated',]
      
class MilestonesKanban7(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['milestones','milestone_description','delivery','updated',]

class CostKanban8(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['invoice','invoice_info','amount','updated']

class AcceptanceKanban9(ModelForm):
    class Meta:
        model = SOWKanban
        fields = ['firstName','firstSignature','date_signature1',
                    'secondName','secondSignature','date_signature2','updated',]


# Scrumban Statement of Work database fields
class SOWScrumban(models.Model):
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
    firstSignature = models.TextField(blank=True)
    date_signature1 = models.DateField(default=datetime.date.today)
    secondName = models.TextField(blank=True)
    secondSignature = models.TextField(blank=True)
    date_signature2 = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField('Last updated', default=datetime.date.today)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SOWScrumban, self).save(*args, **kwargs)


## Scrumban Model forms set for the forms.py user input ##
class CoverScrumban1(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['title','produced_by','date_project','updated','slug',]

class IntroScrumban2(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['intro','updated']

class ObjectivesScrumban3(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['deliverables','assumptions','updated',]

class ScopeScrumban4(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['inScope','outScope','updated',]

class BacklogScrumban5(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['backlog','updated',]

class ScrumbanFrom6(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['plan','iterations','team','wipLimit','review','updated',]
       
class MilestonesScrumban7(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['milestones','milestone_description','delivery','updated',]

class CostScrumban8(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['invoice','invoice_info','amount','updated']

class AcceptanceScrumban9(ModelForm):
    class Meta:
        model = SOWScrumban
        fields = ['firstName','firstSignature','date_signature1',
                    'secondName','secondSignature','date_signature2','updated',]

