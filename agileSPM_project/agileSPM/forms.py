from django import forms
from agileSPM.models import SOW, Scrum, Kanban, Scrumban
import datetime

## Statement of Work models are divided into smaller forms as each form 
# sits on an individual page. ## 

class CoverForm1(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    produced_by = forms.CharField(max_length=128, widget=forms.TextInput)
    date_project = forms.DateField(widget=forms.SelectDateWidget)
    updated = forms.DateTimeField(widget=forms.HiddenInput())
    slug = forms.SlugField(widget=forms.HiddenInput())

    # class Meta:
    #     model = SOW
    #     exclude = ('intro','deliverables','assumptions','milestone_description','date_signature1','date_signature2',
    #                 'inScope','outScope','backlog','milestones','delivery','invoice_info',
    #                 'invoice','amount','firstName','secondName','firstSignature','secondSignature')

class IntroForm2(forms.Form):
    intro = forms.CharField(widget=forms.Textarea)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = SOW
    #     exclude = ('slug','deliverables','assumptions','milestone_description',
    #                 'inScope','outScope','backlog','milestones','delivery','invoice_info',
    #                 'invoice','amount','firstName','secondName','firstSignature','secondSignature',
    #                 'title','produced_by','date_project','date_signature1','date_signature2')

class ObjectivesForm3(forms.Form):
    deliverables = forms.CharField(widget=forms.Textarea)
    assumptions = forms.CharField(widget=forms.Textarea)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = SOW
    #     exclude = ('slug','intro','milestone_description', 'invoice_info',
    #                 'inScope','outScope','backlog','milestones','delivery',
    #                 'invoice','amount','firstName','secondName','firstSignature','secondSignature',
    #                 'title','produced_by','date_project','date_signature1','date_signature2')

class ScopeForm4(forms.Form):
    inScope = forms.CharField(widget=forms.Textarea)
    outScope = forms.CharField(widget=forms.Textarea)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = SOW
    #     exclude = ('slug','deliverables','assumptions','milestone_description',
    #                 'intro','backlog','milestones','delivery','invoice_info',
    #                 'invoice','amount','firstName','secondName','firstSignature','secondSignature',
    #                 'title','produced_by','date_project','date_signature1','date_signature2')

class BacklogForm5(forms.Form):
     backlog = forms.CharField(widget=forms.Textarea)
     updated = forms.DateTimeField(widget=forms.HiddenInput())

    #  class Meta:
    #      model = SOW
    #      exclude = ('slug','deliverables','assumptions','milestone_description',
    #                 'inScope','outScope','intro','milestones','delivery', 'invoice_info',
    #                 'invoice','amount','firstName','secondName','firstSignature','secondSignature',
    #                 'title','produced_by','date_project','date_signature1','date_signature2')

class MilestonesForm7(forms.Form):
    milestones = forms.DateField(widget=forms.SelectDateWidget) 
    milestone_description = forms.CharField(widget=forms.Textarea) 
    delivery = forms.DateField(widget=forms.SelectDateWidget)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = SOW
    #     exclude = ('slug','deliverables','assumptions', 'invoice_info'
    #                 'inScope','outScope','intro', 'backlog',
    #                 'invoice','amount','firstName','secondName','firstSignature','secondSignature',
    #                 'title','produced_by','date_project','date_signature1','date_signature2')

class CostForm8(forms.Form):
    invoice = forms.DateField(widget=forms.SelectDateWidget)
    invoice_info = forms.CharField(max_length=128, widget=forms.TextInput)
    amount = forms.FloatField(widget=forms.TextInput)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = SOW
    #     exclude = ('slug','deliverables','assumptions','milestone_description',
    #                 'inScope','outScope','intro','milestones','delivery', 
    #                 'firstName','secondName','firstSignature','secondSignature',
    #                 'title','produced_by','date_project','date_signature1','date_signature2')

class AcceptanceForm9(forms.Form):
    firstName = forms.CharField(widget=forms.Textarea)
    firstSignature = forms.CharField(widget=forms.Textarea)
    date_signature1 = forms.DateField(widget=forms.SelectDateWidget)
    secondName = forms.CharField(widget=forms.Textarea)
    secondSignature = forms.CharField(widget=forms.Textarea)
    date_signature2 = forms.DateField(widget=forms.SelectDateWidget)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = SOW
    #     exclude = ('slug','deliverables','assumptions','milestone_description',
    #                 'inScope','outScope','intro','milestones','delivery', 'invoice_info',
    #                 'invoice','amount','title','produced_by')
                    

class ScrumForm6(forms.Form):
    sprintLength = forms.IntegerField(widget=forms.TextInput)
    sprint = forms.IntegerField(widget=forms.TextInput)
    sprintPlan = forms.CharField(widget=forms.Textarea)
    team = forms.CharField(widget=forms.Textarea)
    done = forms.CharField(widget=forms.Textarea)
    review = forms.CharField(widget=forms.Textarea)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = Scrum
    #     exclude = ('title',)

class KanbanForm6(forms.Form):
    plan = forms.CharField(widget=forms.Textarea)
    columns = forms.IntegerField(widget=forms.TextInput)
    column_labels = forms.CharField(widget=forms.Textarea)
    wipLimit = forms.IntegerField(widget=forms.TextInput)
    delivery = forms.DateField(widget=forms.SelectDateWidget)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = Kanban
    #     exclude = ('title',)

class ScrumbanForm6(forms.Form):
    plan = forms.CharField(widget=forms.Textarea)
    iterations = forms.IntegerField(widget=forms.TextInput)
    team = forms.CharField(widget=forms.Textarea)
    wipLimit = forms.IntegerField(widget=forms.TextInput)
    review = forms.CharField(widget=forms.Textarea)
    updated = forms.DateTimeField(widget=forms.HiddenInput())

    # class Meta:
    #     model = Scrumban
    #     exclude = ('title',)