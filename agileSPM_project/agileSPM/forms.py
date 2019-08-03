from django import forms
from django.forms import ModelForm
from .models import SOW, Scrum, Kanban, Scrumban, UserProfile
from django.contrib.auth.models import User
import datetime

# User forms & Login/Sign up forms 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User 
        fields = ('username','email','password')

    # method ensuring the email provided does not already exist in database.
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The email you have chosen already exists, please choose another.")
        return email

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

## Statement of Work models are divided into smaller forms as each form 
# sits on an individual page. The use the formstools wizard to combine.## 

### CHECK OUT MODEL FORM SETS FOR MILESTONES AND INVOICES #######

class CoverForm1(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    produced_by = forms.CharField(max_length=128, widget=forms.TextInput)
    date_project = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())
    # slug = forms.SlugField(widget=forms.HiddenInput())

class IntroForm2(forms.Form):
    intro = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ObjectivesForm3(forms.Form):
    deliverables = forms.CharField(widget=forms.Textarea)
    assumptions = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ScopeForm4(forms.Form):
    inScope = forms.CharField(widget=forms.Textarea)
    outScope = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class BacklogForm5(forms.Form):
     backlog = forms.CharField(widget=forms.Textarea)
    #  updated = forms.DateTimeField(widget=forms.HiddenInput())

class MilestonesForm7(forms.Form):
    milestones = forms.DateField(widget=forms.SelectDateWidget) 
    milestone_description = forms.CharField(widget=forms.Textarea) 
    delivery = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class CostForm8(forms.Form):
    invoice = forms.DateField(widget=forms.SelectDateWidget)
    invoice_info = forms.CharField(max_length=128, widget=forms.TextInput)
    amount = forms.FloatField(widget=forms.TextInput)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class AcceptanceForm9(forms.Form):
    firstName = forms.CharField(widget=forms.Textarea)
    firstSignature = forms.CharField(widget=forms.Textarea)
    date_signature1 = forms.DateField(widget=forms.SelectDateWidget)
    secondName = forms.CharField(widget=forms.Textarea)
    secondSignature = forms.CharField(widget=forms.Textarea)
    date_signature2 = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())                    

class ScrumForm6(forms.Form):
    sprintLength = forms.IntegerField(widget=forms.TextInput)
    sprint = forms.IntegerField(widget=forms.TextInput)
    sprintPlan = forms.CharField(widget=forms.Textarea)
    team = forms.CharField(widget=forms.Textarea)
    done = forms.CharField(widget=forms.Textarea)
    review = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class KanbanForm6(forms.Form):
    plan = forms.CharField(widget=forms.Textarea)
    columns = forms.IntegerField(widget=forms.TextInput)
    column_labels = forms.CharField(widget=forms.Textarea)
    wipLimit = forms.IntegerField(widget=forms.TextInput)
    delivery = forms.DateField(widget=forms.SelectDateWidget)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())

class ScrumbanForm6(forms.Form):
    plan = forms.CharField(widget=forms.Textarea)
    iterations = forms.IntegerField(widget=forms.TextInput)
    team = forms.CharField(widget=forms.Textarea)
    wipLimit = forms.IntegerField(widget=forms.TextInput)
    review = forms.CharField(widget=forms.Textarea)
    # updated = forms.DateTimeField(widget=forms.HiddenInput())
