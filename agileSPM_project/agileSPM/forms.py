from django import forms
from django.forms import ModelForm
from .models import SOWScrum, SOWKanban, SOWScrumban
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
import datetime
from django.views.generic.edit import UpdateView

# User forms for sign up
# Overriding the existing help_text with nothing to make sign up page cleaner.
# class UserForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forms', 'id':'username'}), help_text='', required=True)
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'forms', 'id':'email'}),help_text='', required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forms', 'id':'password1'}),help_text='', required=True, label='Password')
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forms', 'id':'password2'}),help_text='', required=True, label='Repeat Password')

#     class Meta:
#         model = User
#         fields = ['username','email','password1', 'password2']

class RegisterForm(UserCreationForm):
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

class SignUpModalForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forms', 'id':'username'}), help_text='', required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'forms', 'id':'email'}),help_text='', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forms', 'id':'password1'}),help_text='', required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forms', 'id':'password2'}),help_text='', required=True, label='Repeat Password')

    class Meta: 
        model = User
        fields = ['username','email','password1','password2']


class DateInput(forms.DateInput):
    input_type = 'date'

## Model form used to get input from user to populate specific document.
class SOWScrumForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'error'

    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'titleID', 'spellcheck': 'true', 'placeholder':'Enter the title name' }),label='Project Title')
    produced_by = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'id':'producedID', 'spellcheck': 'true', 'placeholder': 'Author of the statement of work'}), label='Produced By', required="False")
    date_project = forms.DateField(widget=DateInput(attrs={'id':'dateprojID'}), label="Today's date",required="False")
    intro = forms.CharField(widget=forms.Textarea(attrs={'id':'introID', 'spellcheck': 'true', 'placeholder': 'A brief introduction into your project and what is meant to be achieved with it'}), label='Introduction',required="False")
    deliverables = forms.CharField(widget=forms.Textarea(attrs={'id':'deliverablesID', 'spellcheck': 'true', 'placeholder': 'Key measurable deliverables to be achieved by this project' }), label='Project Deliverables',required="False")
    assumptions = forms.CharField(widget=forms.Textarea(attrs={'id':'assumptionsID', 'spellcheck': 'true', 'placeholder':'Any technical assumptions, non-functional requirements or assumptions made about the project that are relevant'}), label='Assumptions made',required="False")
    inScope = forms.CharField(widget=forms.Textarea(attrs={'id':'scopeID', 'spellcheck': 'true', 'placeholder': 'Deliverables and overall objectives included in this project'}), label='In Scope',required="False")
    outScope = forms.CharField(widget=forms.Textarea(attrs={'id':'outscopeID', 'spellcheck': 'true', 'placeholder':'Elements of development that are not specific to the project at hand'}), label='Out of Scope',required="False")
    backlog = forms.CharField(widget=forms.Textarea(attrs={'id':'backlogID', 'spellcheck': 'true', 'placeholder':'Tasks, user stories, epics or bugs all relating to the project at hand'}), label='Product Backlog',required="False")
    sprintLength = forms.IntegerField(widget=forms.TextInput(attrs={'id':'lengthID', 'spellcheck': 'true', 'placeholder':'Length of each sprint of the project'}), label='Length of Sprint in Weeks',required="False")
    sprint = forms.IntegerField(widget=forms.TextInput(attrs={'id':'sprintID', 'spellcheck': 'true', 'placeholder': 'The number of sprints included in this project'}), label='Number of Sprints',required="False")
    sprintPlan = forms.CharField(widget=forms.Textarea(attrs={'id':'planID', 'spellcheck': 'true', 'placeholder': 'Details surrounding the delivery of the sprint, information all parties should know before starting'}), label='Sprint Plan',required="False")
    team = forms.CharField(widget=forms.Textarea(attrs={'id':'teamID', 'spellcheck': 'true', 'placeholder':'Team members involved in the project and their roles'}), label='Team members',required="False")
    done = forms.CharField(widget=forms.Textarea(attrs={'id':'doneID', 'spellcheck': 'true', 'placeholder': 'An overall defintion of done to check back against for validation'}), label='Defining Done',required="False")
    review = forms.CharField(widget=forms.Textarea(attrs={'id':'reviewID', 'spellcheck': 'true', 'placeholder': 'Include any review opportunities at certain stages of the development'}), label='Sprint review',required="False")
    milestones = forms.DateField(widget=DateInput(attrs={'id':'milestonesID'}), label='Milestones',required="False")
    milestone_description = forms.CharField(widget=forms.Textarea(attrs={'id':'milestonedescID', 'spellcheck': 'true', 'placeholder':'Describe why the milestone is set to that date and its importance to the project'}),label='Description',required="False") 
    delivery = forms.DateField(widget=DateInput(attrs={'id':'deliveryID'}), label='Delivery date',required="False")
    invoice = forms.DateField(widget=DateInput(attrs={'id':'invoiceID'}),label='Invoice date',required="False")
    invoice_info = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'id':'invoiceinfoID', 'spellcheck': 'true', 'placeholder':'Describe what the invoice is for, if it is the whole amount or a partial amount of the whole project budget'}), label='Description',required="False")
    amount = forms.CharField(widget=forms.TextInput(attrs={'id':'amountID', 'placeholder':'Amount to be invoiced without £'}), label='Invoice Total',required="False")
    firstName = forms.CharField(widget=forms.Textarea(attrs={'id':'nameoneID', 'spellcheck': 'true', 'placeholder':'Your name goes here'}), label='First Signature Full Name',required="False")
    date_signature1 = forms.DateField(widget=DateInput(attrs={'id':'datesign-oneID'}), label='Date',required="False")
    secondName = forms.CharField(widget=forms.Textarea(attrs={'id':'nametwoID', 'spellcheck': 'true', 'placeholder':'Second party name goes here'}), label='Second Signature Full Name',required="False")
    date_signature2 = forms.DateField(widget=DateInput(attrs={'id':'datesign-twoID'}), label='Date',required="False")

    class Meta:
        model = SOWScrum
        widgets = {'date_widget': DateInput()}
        fields = ['title','produced_by','date_project',
                    'intro','deliverables','assumptions','inScope','outScope',
                    'backlog','sprintLength','sprint','sprintPlan','team','done',
                    'review','milestones', 'milestone_description','delivery','invoice',
                    'invoice','invoice_info','amount','firstName',
                    'date_signature1','secondName','date_signature2',]


# Editable form from User's collection of finished and unfinished documents
class EditScrumForm(forms.Form):

    class Meta: 
        model = SOWScrum
        fields = ['title','produced_by','date_project',
                    'intro','deliverables','assumptions','inScope','outScope',
                    'backlog','sprintLength','sprint','sprintPlan','team','done',
                    'review','milestones', 'milestone_description','delivery','invoice',
                    'invoice','invoice_info','amount','firstName',
                    'date_signature1','secondName','date_signature2',]  

        template_name_suffix = '_edit_form'   



## Model form used to get input from user to populate specific document.
class SOWKanbanForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.Textarea, label='Project Title')
    # produced_by = forms.CharField(max_length=128, widget=forms.TextInput, label='Produced By')
    # date_project = forms.DateField(widget=forms.SelectDateWidget, label="Today's date")
    # intro = forms.CharField(widget=forms.Textarea, label='Introduction')
    # deliverables = forms.CharField(widget=forms.Textarea, label='Project Deliverables')
    # assumptions = forms.CharField(widget=forms.Textarea, label='Assumptions made')
    # inScope = forms.CharField(widget=forms.Textarea, label='In Scope')
    # outScope = forms.CharField(widget=forms.Textarea, label='Out of Scope')
    # backlog = forms.CharField(widget=forms.Textarea, label='Backlog')
    # plan = forms.TextField(widget=forms.Textarea, label='Kanban plan')
    # columns = forms.IntegerField(widget=forms.TextInput, label='Number of Kanban columns used')
    # column_labels = forms.TextField(widget=forms.TextInput, label='Labels used in Kanban columns')
    # wipLimit = forms.IntegerField(widget=forms.TextInput, label='Work In Progress (WIP) limit')
    # milestones = forms.DateField(widget=forms.SelectDateWidget, label='Milestones') 
    # milestone_description = forms.CharField(widget=forms.Textarea,label='Description') 
    # delivery = forms.DateField(widget=forms.SelectDateWidget, label='Delivery date')
    # invoice = forms.DateField(widget=forms.SelectDateWidget,label='Invoice date')
    # invoice_info = forms.CharField(max_length=128, widget=forms.TextInput, label='Description')
    # amount = forms.FloatField(widget=forms.TextInput, label='Invoice Total')
    # firstName = forms.CharField(widget=forms.Textarea, label='First Signature Full Name')
    # date_signature1 = forms.DateField(widget=forms.SelectDateWidget, label='Date')
    # secondName = forms.CharField(widget=forms.Textarea, label='Second Signature Full Name')
    # date_signature2 = forms.DateField(widget=forms.SelectDateWidget, label='Date')

    class Meta:
        model = SOWScrum
        fields = ['title','produced_by','date_project',
                    'intro','deliverables','assumptions','inScope','outScope',
                    'backlog','sprintLength','sprint','sprintPlan','team','done',
                    'review','milestones', 'milestone_description','delivery','invoice',
                    'invoice','invoice_info','amount','firstName',
                    'date_signature1','secondName','date_signature2',]

    def save(self, commit=True):
        kanban = super(SOWKanbanForm, self).save(commit=False)

        kanban.title = self.cleaned_data['title']
        kanban.produced_by = self.cleaned_data['produced_by']
        kanban.date_project = self.cleaned_data['date_project']
        kanban.intro = self.cleaned_data['intro']
        kanban.deliverables = self.cleaned_data['deliverables']
        kanban.assumptions = self.cleaned_data['assumptions']
        kanban.inScope = self.cleaned_data['inScope']
        kanban.outScope = self.cleaned_data['outScope']
        kanban.backlog = self.cleaned_data['backlog']
        kanban.sprintLength = self.cleaned_data['sprintLength']
        kanban.sprint = self.cleaned_data['sprint']
        kanban.sprintPlan = self.cleaned_data['sprintPlan']
        kanban.team = self.cleaned_data['team']
        kanban.done = self.cleaned_data['done']
        kanban.review = self.cleaned_data['review']
        kanban.milestones = self.cleaned_data['milestones']
        kanban.milestone_description = self.cleaned_data['milestone_desription']
        kanban.delivery = self.cleaned_data['delivery']
        kanban.invoice = self.cleaned_data['invoice']
        kanban.invoice_info = self.cleaned_data['invoice_info']
        kanban.amount = self.cleaned_data['amount']
        kanban.firstName = self.cleaned_data['firstName']
        kanban.date_signature1 = self.cleaned_data['date_signature1']
        kanban.secondName = self.cleaned_data['secondName']
        kanban.date_signature2 = self.cleaned_data['date_signature2']

        if commit:
            kanban.save()
        
        return kanban


## Model form used to get input from user to populate specific document.
class SOWScrumbanForm(forms.ModelForm):
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





