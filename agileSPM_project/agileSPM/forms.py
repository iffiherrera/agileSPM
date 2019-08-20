from django import forms
from django.forms import ModelForm
from .models import SOWScrum, SOWKanban, SOWScrumban, UserProfile
from django.contrib.auth.models import User
import datetime

# User forms & Login/Sign up forms 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User 
        fields = ['username','email','password']

    # method ensuring the email provided does not already exist in database.
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The email you have chosen already exists, please choose another.")
        return email

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture',]

class SOWForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea, label='Project Title')
    produced_by = forms.CharField(max_length=128, widget=forms.TextInput, label='Produced By')
    date_project = forms.DateField(widget=forms.SelectDateWidget, label="Today's date")
    intro = forms.CharField(widget=forms.Textarea, label='Introduction')
    deliverables = forms.CharField(widget=forms.Textarea, label='Project Deliverables')
    assumptions = forms.CharField(widget=forms.Textarea, label='Assumptions made')
    inScope = forms.CharField(widget=forms.Textarea, label='In Scope')
    outScope = forms.CharField(widget=forms.Textarea, label='Out of Scope')
    backlog = forms.CharField(widget=forms.Textarea, label='Backlog')
    sprintLength = forms.IntegerField(widget=forms.TextInput, label='Length of Sprint')
    sprint = forms.IntegerField(widget=forms.TextInput, label='Sprints')
    sprintPlan = forms.CharField(widget=forms.Textarea, label='Sprint Plan')
    team = forms.CharField(widget=forms.Textarea, label='Team')
    done = forms.CharField(widget=forms.Textarea, label='Defining Done')
    review = forms.CharField(widget=forms.Textarea, label='Sprint review')
    milestones = forms.DateField(widget=forms.SelectDateWidget, label='Milestones') 
    milestone_description = forms.CharField(widget=forms.Textarea,label='Description') 
    delivery = forms.DateField(widget=forms.SelectDateWidget, label='Delivery date')
    invoice = forms.DateField(widget=forms.SelectDateWidget,label='Invoice date')
    invoice_info = forms.CharField(max_length=128, widget=forms.TextInput, label='Description')
    amount = forms.FloatField(widget=forms.TextInput, label='Invoice Total')
    firstName = forms.CharField(widget=forms.Textarea, label='First Signature Full Name')
    date_signature1 = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    secondName = forms.CharField(widget=forms.Textarea, label='Second Signature Full Name')
    date_signature2 = forms.DateField(widget=forms.SelectDateWidget, label='Date')

    class Meta:
        model = SOWScrum
        fields = ['title','produced_by','date_project',
                    'intro','deliverables','assumptions','inScope','outScope',
                    'backlog','sprintLength','sprint','sprintPlan','team','done',
                    'review','milestones', 'milestone_description','delivery','invoice',
                    'invoice','invoice_info','amount','firstName',
                    'date_signature1','secondName','date_signature2',]

        

## Statement of Work models are divided into smaller forms as each form 
# sits on an individual page. They use the formstools wizard to combine.## 

### CHECK OUT MODEL FORM SETS FOR MILESTONES AND INVOICES #######

## SCRUM FORM ##
class CoverScrum1(forms.Form):
    title = forms.CharField(widget=forms.Textarea, label='Project Title')
    produced_by = forms.CharField(max_length=128, widget=forms.TextInput, label='Produced By')
    date_project = forms.DateField(widget=forms.SelectDateWidget, label="Today's date")
    # updated = forms.DateTimeField(widget=forms.HiddenInput())
    # slug = forms.SlugField(widget=forms.HiddenInput())

class IntroScrum2(forms.Form):
    intro = forms.CharField(widget=forms.Textarea, label='Introduction')
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ObjectivesScrum3(forms.Form):
    deliverables = forms.CharField(widget=forms.Textarea, label='Project Deliverables')
    assumptions = forms.CharField(widget=forms.Textarea, label='Assumptions made')
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ScopeScrum4(forms.Form):
    inScope = forms.CharField(widget=forms.Textarea, label='In Scope')
    outScope = forms.CharField(widget=forms.Textarea, label='Out of Scope')
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class BacklogScrum5(forms.Form):
     backlog = forms.CharField(widget=forms.Textarea, label='Backlog')
    #  updated = forms.DateTimeField(widget=forms.HiddenInput())

class ScrumForm6(forms.Form):
    sprintLength = forms.IntegerField(widget=forms.TextInput, label='Length of Sprint')
    sprint = forms.IntegerField(widget=forms.TextInput, label='Sprints')
    sprintPlan = forms.CharField(widget=forms.Textarea, label='Sprint Plan')
    team = forms.CharField(widget=forms.Textarea, label='Team')
    done = forms.CharField(widget=forms.Textarea, label='Defining Done')
    review = forms.CharField(widget=forms.Textarea, label='Sprint review')
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class MilestonesScrum7(forms.Form):
    milestones = forms.DateField(widget=forms.SelectDateWidget, label='Milestones') 
    milestone_description = forms.CharField(widget=forms.Textarea,label='Description') 
    delivery = forms.DateField(widget=forms.SelectDateWidget, label='Delivery date')
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class CostScrum8(forms.Form):
    invoice = forms.DateField(widget=forms.SelectDateWidget,label='Invoice date')
    invoice_info = forms.CharField(max_length=128, widget=forms.TextInput, label='Description')
    amount = forms.FloatField(widget=forms.TextInput, label='Invoice Total')
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class AcceptanceScrum9(forms.Form):
    firstName = forms.CharField(widget=forms.Textarea, label='First Signature Full Name')
    firstSignature = forms.CharField(widget=forms.Textarea, label='Signature')
    date_signature1 = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    secondName = forms.CharField(widget=forms.Textarea, label='Second Signature Full Name')
    secondSignature = forms.CharField(widget=forms.Textarea, label='Signature')
    date_signature2 = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    # updated = forms.DateTimeField(widget=forms.HiddenInput())                    

## KANBAN FORM ##
class CoverKanban1(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    produced_by = forms.CharField(max_length=128, widget=forms.TextInput)
    date_project = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())
    # slug = forms.SlugField(widget=forms.HiddenInput())

class IntroKanban2(forms.Form):
    intro = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ObjectivesKanban3(forms.Form):
    deliverables = forms.CharField(widget=forms.Textarea)
    assumptions = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ScopeKanban4(forms.Form):
    inScope = forms.CharField(widget=forms.Textarea)
    outScope = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class BacklogKanban5(forms.Form):
     backlog = forms.CharField(widget=forms.Textarea)
    #  updated = forms.DateTimeField(widget=forms.HiddenInput())

class KanbanForm6(forms.Form):
    plan = forms.CharField(widget=forms.Textarea)
    columns = forms.IntegerField(widget=forms.TextInput)
    column_labels = forms.CharField(widget=forms.Textarea)
    wipLimit = forms.IntegerField(widget=forms.TextInput)
    delivery = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class MilestonesKanban7(forms.Form):
    milestones = forms.DateField(widget=forms.SelectDateWidget) 
    milestone_description = forms.CharField(widget=forms.Textarea) 
    delivery = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class CostKanban8(forms.Form):
    invoice = forms.DateField(widget=forms.SelectDateWidget)
    invoice_info = forms.CharField(max_length=128, widget=forms.TextInput)
    amount = forms.FloatField(widget=forms.TextInput)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class AcceptanceKanban9(forms.Form):
    firstName = forms.CharField(widget=forms.Textarea)
    firstSignature = forms.CharField(widget=forms.Textarea)
    date_signature1 = forms.DateField(widget=forms.SelectDateWidget)
    secondName = forms.CharField(widget=forms.Textarea)
    secondSignature = forms.CharField(widget=forms.Textarea)
    date_signature2 = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

## SCRUMBAN FORM ##

class CoverScrumban1(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    produced_by = forms.CharField(max_length=128, widget=forms.TextInput)
    date_project = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())
    # slug = forms.SlugField(widget=forms.HiddenInput())

class IntroScrumban2(forms.Form):
    intro = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ObjectivesScrumban3(forms.Form):
    deliverables = forms.CharField(widget=forms.Textarea)
    assumptions = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ScopeScrumban4(forms.Form):
    inScope = forms.CharField(widget=forms.Textarea)
    outScope = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class BacklogScrumban5(forms.Form):
     backlog = forms.CharField(widget=forms.Textarea)
    #  updated = forms.DateTimeField(widget=forms.HiddenInput())

class ScrumbanForm6(forms.Form):
    plan = forms.CharField(widget=forms.Textarea)
    iterations = forms.IntegerField(widget=forms.TextInput)
    team = forms.CharField(widget=forms.Textarea)
    wipLimit = forms.IntegerField(widget=forms.TextInput)
    review = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class MilestonesScrumban7(forms.Form):
    milestones = forms.DateField(widget=forms.SelectDateWidget) 
    milestone_description = forms.CharField(widget=forms.Textarea) 
    delivery = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class CostScrumban8(forms.Form):
    invoice = forms.DateField(widget=forms.SelectDateWidget)
    invoice_info = forms.CharField(max_length=128, widget=forms.TextInput)
    amount = forms.FloatField(widget=forms.TextInput)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class AcceptanceScrumban9(forms.Form):
    firstName = forms.CharField(widget=forms.Textarea)
    firstSignature = forms.CharField(widget=forms.Textarea)
    date_signature1 = forms.DateField(widget=forms.SelectDateWidget)
    secondName = forms.CharField(widget=forms.Textarea)
    secondSignature = forms.CharField(widget=forms.Textarea)
    date_signature2 = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())




