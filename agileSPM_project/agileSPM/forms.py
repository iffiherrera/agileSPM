from django import forms
from django.forms import ModelForm
from .models import SOWScrum, SOWKanban, SOWScrumban, UserProfile
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
import datetime
from django.views.generic.edit import UpdateView

# User forms for sign up
# Overriding the existing help_text with nothing to make sign up page cleaner.
class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forms', 'id':'username'}), help_text='', required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'forms', 'id':'email'}),help_text='', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forms', 'id':'password1'}),help_text='', required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forms', 'id':'password2'}),help_text='', required=True, label='Repeat Password')

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

    # method ensuring the email provided does not already exist in database.
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The email you have chosen already exists, please choose another.")
        return email

    # commit only if data is valid and in right format.
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        
        return user


## Model form used to get input from user to populate specific document.
class SOWScrumForm(forms.ModelForm):
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

    def save(self, commit=True):
        scrum = super(SOWSrumForm, self).save(commit=False)

        scrum.title = self.cleaned_data['title']
        scrum.produced_by = self.cleaned_data['produced_by']
        scrum.date_project = self.cleaned_data['date_project']
        scrum.intro = self.cleaned_data['intro']
        scrum.deliverables = self.cleaned_data['deliverables']
        scrum.assumptions = self.cleaned_data['assumptions']
        scrum.inScope = self.cleaned_data['inScope']
        scrum.outScope = self.cleaned_data['outScope']
        scrum.backlog = self.cleaned_data['backlog']
        scrum.sprintLength = self.cleaned_data['sprintLength']
        scrum.sprint = self.cleaned_data['sprint']
        scrum.sprintPlan = self.cleaned_data['sprintPlan']
        scrum.team = self.cleaned_data['team']
        scrum.done = self.cleaned_data['done']
        scrum.review = self.cleaned_data['review']
        scrum.milestones = self.cleaned_data['milestones']
        scrum.milestone_description = self.cleaned_data['milestone_desription']
        scrum.delivery = self.cleaned_data['delivery']
        scrum.invoice = self.cleaned_data['invoice']
        scrum.invoice_info = self.cleaned_data['invoice_info']
        scrum.amount = self.cleaned_data['amount']
        scrum.firstName = self.cleaned_data['firstName']
        scrum.date_signature1 = self.cleaned_data['date_signature1']
        scrum.secondName = self.cleaned_data['secondName']
        scrum.date_signature2 = self.cleaned_data['date_signature2']

        if commit:
            scrum.save()
        
        return scrum

# Editable form from User's collection of finished and unfinished documents
class EditScrumForm(UpdateView):

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





