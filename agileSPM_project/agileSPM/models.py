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

## Model forms set for the forms.py user input ##
class CoverFrom1(ModelForm):
    class Meta:
        model = SOW
        fields = ['title','produced_by','date_project','updated','slug',]

class IntroForm2(ModelForm):
    class Meta:
        model = SOW
        fields = ['intro','updated']

class ObjectivesForm3(ModelForm):
    class Meta:
        model = SOW
        fields = ['deliverables','assumptions','updated',]

class ScopeForm4(ModelForm):
    class Meta:
        model = SOW
        fields = ['inScope','outScope','updated',]

class BacklogForm5(ModelForm):
    class Meta:
        model = SOW
        fields = ['backlog','updated',]

class ScrumForm6(ModelForm):
    class Meta: 
        model = Scrum
        fields = ['sprintPlan','sprintLength','sprint','team','done','review','updated',]
        exclude = ['title',]

class KanbanForm6(ModelForm):
    class Meta:
        model = Kanban
        fields = ['plan','columns','column_labels','wipLimit','delivery','updated',]
        exclude = ['title',]

class ScrumbanFrom6(ModelForm):
    class Meta:
        model = Scrumban
        fields = ['plan','iterations','team','wipLimit','review','updated',]
        exclude = ['title',]

class MilestonesForm7(ModelForm):
    class Meta:
        model = SOW
        fields = ['milestones','milestone_description','delivery','updated',]

class CostForm8(ModelForm):
    class Meta:
        model = SOW
        fields = ['invoice','invoice_info','amount','updated']

class AcceptanceForm9(ModelForm):
    class Meta:
        model = SOW
        fields = ['firstName','firstSignature','date_signature1',
                    'secondName','secondSignature','date_signature2','updated',]





