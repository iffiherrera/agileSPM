from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from .models import SOWScrum, SOWKanban, SOWScrumban
from .forms import CoverScrum1, IntroScrum2, ObjectivesScrum3, ScopeScrum4, ScrumForm6, BacklogScrum5, MilestonesScrum7, CostScrum8, AcceptanceScrum9, UserForm, UserProfileForm
from .forms import CoverKanban1, IntroKanban2, ObjectivesKanban3, ScopeKanban4, BacklogKanban5, KanbanForm6, MilestonesKanban7, CostKanban8, AcceptanceKanban9
from .forms import CoverScrumban1, IntroScrumban2, ObjectivesScrumban3, ScopeScrumban4, BacklogScrumban5, ScrumbanForm6, MilestonesScrumban7, CostScrumban8, AcceptanceScrumban9
from formtools.wizard.views import WizardView, SessionWizardView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# from formtools.preview import FormPreview

# Forms for URL mapping.
KANBAN_FORM = (
    ("Cover", CoverKanban1),
    ("Intro", IntroKanban2),
    ("Objectives", ObjectivesKanban3),
    ("Scope", ScopeKanban4),
    ("Backlog", BacklogKanban5),
    ("Kanban", KanbanForm6),
    ("Milestones", MilestonesKanban7),
    ("Cost", CostKanban8),
    ("Acceptance", AcceptanceKanban9),
)
# Forms for URL mapping.
SCRUMBAN_FORM = (
    ("Cover", CoverScrumban1),
    ("Intro", IntroScrumban2),
    ("Objectives", ObjectivesScrumban3),
    ("Scope", ScopeScrumban4),
    ("Backlog", BacklogScrumban5),
    ("Scrumban", ScrumbanForm6),
    ("Milestones", MilestonesScrumban7),
    ("Cost", CostScrumban8),
    ("Acceptance", AcceptanceScrumban9),
)

# Home view 
def index(request):
    user_form = UserForm()
    profile_form = UserProfileForm()

    context_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'agileSPM/index.html', context=context_dict)

# User account view 
@login_required()
def my_docs(request):
    user_form = UserForm()
    profile_form = UserProfileForm()
    profile = UserProfile.objects.filter(user=request.user)[0]

    context_dict = {'user_form': user_form,
                    'profile_form': profile_form,
                    'profile': profile,}

    return render(request, 'agile/SPM/docs.html', context=context_dict)

# Pop up login/sign up function using Ajax function and modal
def login_popup(request):
    context_dict = {}
    if request.method == 'POST':
        # Request and validate username/password.
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return JsonResponse({'login': True})
            else:
                context_dict['error'] = "Account is no longer active"
                return JsonResponse({'login': False,
                                        'error': context_dict['error']})
        else:
            context_dict['error'] = "Username and password do not match. Please try again."
            print("Invalid:{0},{1}".format(username,password))
            return JsonResponse({'login': False,
                                        'error': context_dict['error']})
    else:
        context_dict['action'] = 'login'
        return render(request,'agileSPM/index.html', context=context_dict)

# User logout ability
@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Registration form completion and save to database
def register(request):
    registered = False # Initially set to false because registration is not completed.

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Saves user and profile input to database.
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False) # only commit when the whole form is completed.
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True # Sets registration to true at this point.
        else:
            print(user_form.errors, profile_form.errors) # prints errors to terminal for testing/QA
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'agileSPM/register.html', {'user_form' : user_form,
                                                       'profile_form' : profile_form,
                                                       'registered' : registered, })    

# Form view 
# def input_doc(request):
#     form1 =  CoverForm1()

#     if request.method == 'POST':
#         form1 = CoverForm1(request.POST)

#         if form1.is_valid():
#             form1.save(commit=True)
#             return index(request)

#         else:
#             print(form1.errors)
#     return render(request, 'agileSPM/index.html', {'form': form1})

# Scrum specific form view
class Scrum_Sow_Wizard(SessionWizardView):
    template_name = "agileSPM/wizard/scrum_sow_template.html"
    model = SOWScrum
    form_list= [CoverScrum1,IntroScrum2,ObjectivesScrum3,ScopeScrum4,
                BacklogScrum5,ScrumForm6,MilestonesScrum7,
                CostScrum8,AcceptanceScrum9]
    print(form_list)
    
    # Restores information from session to session.
    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError: 
            return super().get(request,*args,**kwargs)

    # Processes the whole document once it's completed.
    def done(self, form_list, **kwargs):
        
        form_data = [form.cleaned_data for form in form_list]
        
        # Objects created from the user's input to populate document.
        title_scrum = form_data[0]['title']
        produced_scrum = form_data[0]['produced_by']
        date_scrum = form_data[0]['date_project']
        intro_scrum = form_data[1]['intro']
        deliverables_scrum = form_data[2]['deliverables']
        assumptions_scrum = form_data[2]['assumptions']
        scopeIn_scrum = form_data[3]['inScope']
        scopeOut_scrum = form_data[3]['outScope']
        backlog_scrum = form_data[4]['backlog']
        sprint_length_scrum = form_data[5]['sprintLength']
        sprint_scrum = form_data[5]['sprint']
        sprint_plan_scrum = form_data[5]['sprintPlan']
        team_scrum = form_data[5]['team']
        done_scrum = form_data[5]['done']
        review_scrum = form_data[5]['review']
        milestones_scrum = form_data[6]['milestones']
        milestone_description_scrum = form_data[6]['milestone_description']
        delivery_scrum = form_data[6]['delivery']
        invoice_scrum = form_data[7]['invoice']
        invoice_info_scrum = form_data[7]['invoice_info']
        invoice_amount_scrum = form_data[7]['amount']
        firstName_scrum = form_data[8]['firstName']
        firstSignature_scrum = form_data[8]['firstSignature']
        date_signature1_scrum = form_data[8]['date_signature1']
        secondName_scrum = form_data[8]['secondName']
        secondSignature_scrum = form_data[8]['secondSignature']
        date_signature2 = form_data[8]['date_signature2']

        dictionary = SOWScrum(**form_data)
        dictionary.save()

        print('output', dictionary)

        return render(self.request, 'agileSPM/wizard/done.html',{
            'form_data': form_data,})

# Kanban specific form view
class Kanban_Sow_Wizard(SessionWizardView):
    template_name = "agileSPM/wizard/kanban_sow_template.html"
    form_list = [KANBAN_FORM]
    
    # Restores information from session to session.
    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError: 
            return super().get(request,*args,**kwargs)

    # Processes the whole document once it's completed.
    def done(self, form_list, **kwargs):
        return render(self.request,'agileSPM/wizard/done.html',{
            'form_data': [form.cleaned_data for form in form_list]
        })
       

# Scrumban specific form view
class Scrumban_Sow_Wizard(SessionWizardView):
    template_name = "agileSPM/wizard/scrumban_sow_template.html"
    form_list = [SCRUMBAN_FORM]
    
    # Restores information from session to session.
    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError: 
            return super().get(request,*args,**kwargs)

    # Processes the whole document once it's completed.
    def done(self, form_list, **kwargs):
        return render(self.request,'agileSPM/wizard/done.html',{
            'form_data': [form.cleaned_data for form in form_list]
        })
        

# Scrum Document creation using docx-Python API
def scrum_doc(request):

## Document formatting, rules & styles ##
    s_project = Document()
    paragraph = s_project.add_paragraph()
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.keep_with_next = True

    styles = s_project.styles
    body_text_style = s_project.styles['Body Text']
    list_bullet_style = s_project.styles['List Bullet']
    numbered_bullet_style = s_project.styles['ListNumber']
    # title_scrum = form_data[0]['title']

## Cover page ##

    # Title
    s_project.add_heading('title_scrum', 0)
    # Produced by 
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Date created
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    s_project.add_page_break()

## Overview ##

    # Introduction
    s_project.add_heading('Introduction', level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Objectives ##

    # Deliverables 
    s_project.add_heading('Deliverables',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)
    # Assumptions
    s_project.add_heading('Assumptions',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Scope ##

    # In Scope
    s_project.add_heading('In Scope',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Out of Scope
    s_project.add_heading('Out of Scope',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Backlog ##

    # Product backlog 
    s_project.add_heading('Product backlog',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Mode of Delivery ##

    # Sprint plan 
    s_project.add_heading('Sprint Planning',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Sprints
    para = s_project.add_paragraph('Number of Sprints:')
    para.add_run('Number goes here').bold = True
    # Sprint Length
    para = s_project.add_paragraph('Length of Sprint:')
    para.add_run('Number goes here').bold = True
    # Team 
    s_project.add_heading('Team Structure',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Done
    s_project.add_heading('Defining Done',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Review
    s_project.add_heading('Review Opportunities',level=1)
    s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
  

## Milestones ## 

    # Milestones table 
    s_project.add_heading('Milestones',level=1)
    milestone_table = s_project.add_table(rows=3, cols=2)
    milestone_table.style = 'LightShading-Accent1'
    header_cells = milestone_table.rows[0].cells
    header_cells[0].text = 'Milestone'
    header_cells[1].text = 'Date'
    row = milestone_table.add_row() # Method adding a row, to be called! 
    # Delivery
    para = s_project.add_paragraph('Delivery date:')
    para.add_run('Number goes here').bold = True

    for row in milestone_table.rows:
        for cell in row.cells:
            print(cell.text)

## Costs ## 

    # Invoice schedule table
    s_project.add_heading('Invoice schedule',level=1)
    invoice_table = s_project.add_table(rows=3, cols=3)
    invoice_table.style = 'LightShading-Accent1'
    header_cells = invoice_table.rows[0].cells
    header_cells[0].text = 'Invoice number'
    header_cells[1].text = 'Date'
    header_cells[2].text = 'Total'
    row = invoice_table.add_row() # Method adding a row, to be called! 

    for row in invoice_table.rows:
            for cell in row.cells:
                print(cell.text)

## Acceptance ##

    # Signature 1
    s_project.add_heading('Acceptance',level=1)
    s_project.add_paragraph('Full name:', style=body_text_style)
    s_project.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = s_project.add_paragraph('Date signed:')
    para.add_run('Number goes here')
    # Signature 2
    s_project.add_paragraph('Full name:', style=body_text_style)
    s_project.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = s_project.add_paragraph('Date signed:')
    para.add_run('Number goes here')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=ScrumProject.docx'
    s_project.save(response)
    return response

    return render(request, {'form data' : form_data})

# Kanban Document creation using docx-Python API
def kanban_doc(request):

## Document formatting,rules & styles ##
    k_project = Document()
    paragraph = k_project.add_paragraph()
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.keep_with_next = True

    styles = k_project.styles
    body_text_style = k_project.styles['Body Text']
    list_bullet_style = k_project.styles['List Bullet']
    numbered_bullet_style = k_project.styles['ListNumber']

## Cover page ##

    # Title
    k_project.add_heading('Scrum Project', 0)
    # Produced by 
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Date created
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    k_project.add_page_break()

## Overview ##

    # Introduction
    k_project.add_heading('Introduction', level=1)
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Objectives ##

    # Deliverables 
    k_project.add_heading('Deliverables',level=1)
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)
    # Assumptions
    k_project.add_heading('Assumptions',level=1)
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Scope ##

    # In Scope
    k_project.add_heading('In Scope',level=1)
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Out of Scope
    k_project.add_heading('Out of Scope',level=1)
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Backlog ##

    # Product backlog 
    k_project.add_heading('Product backlog',level=1)
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Mode of Delivery ##

    # Kanban plan 
    k_project.add_heading('Kanban Overview',level=1)
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Columns
    para = k_project.add_paragraph('Number of Columns used in board:')
    para.add_run('Number goes here').bold = True
    # Labels
    k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # WIP limit
    para = k_project.add_paragraph('Work In Progress limit:')
    para.add_run('Number goes here').bold = True
    # Delivery
    para = k_project.add_paragraph('Delivery date:')
    para.add_run('Number goes here').bold = True

## Costs ## 

    # Invoice schedule table
    k_project.add_heading('Invoice schedule',level=1)
    invoice_table = k_project.add_table(rows=3, cols=3)
    invoice_table.style = 'LightShading-Accent1'
    header_cells = invoice_table.rows[0].cells
    header_cells[0].text = 'Invoice number'
    header_cells[1].text = 'Date'
    header_cells[2].text = 'Total'
    row = invoice_table.add_row() # Method adding a row, to be called! 

    for row in table.rows:
            for cell in rows.cells:
                print(cell.text)

## Acceptance ##

    # Signature 1
    k_project.add_heading('Acceptance',level=1)
    k_project.add_paragraph('Full name:', style=body_text_style)
    k_project.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = k_project.add_paragraph('Date signed:')
    para.add_run('Number goes here')
    # Signature 2
    k_project.add_paragraph('Full name:', style=body_text_style)
    k_project.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = k_project.add_paragraph('Date signed:')
    para.add_run('Number goes here')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=KanbanProject.docx'
    k_project.save(response)
    return response

# Scrumban Document creation using docx-Python API
def scrumban_doc(request):

## Document formatting, styles and rules ##
    sb_project = Document()

    paragraph = sb_project.add_paragraph()
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.keep_with_next = True

    styles = sb_project.styles
    body_text_style = sb_project.styles['Body Text']
    list_bullet_style = sb_project.styles['List Bullet']
    numbered_bullet_style = sb_project.styles['ListNumber']

## Cover page ##

    # Title
    sb_project.add_heading('Scrum Project', 0)
    # Produced by 
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Date created
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    sb_project.add_page_break()

## Overview ##

    # Introduction
    sb_project.add_heading('Introduction', level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Objectives ##

    # Deliverables 
    sb_project.add_heading('Deliverables',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)
    # Assumptions
    sb_project.add_heading('Assumptions',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Scope ##

    # In Scope
    sb_project.add_heading('In Scope',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Out of Scope
    sb_project.add_heading('Out of Scope',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Backlog ##

    # Product backlog 
    sb_project.add_heading('Product backlog',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Mode of Delivery ##

    # Scrumban plan 
    sb_project.add_heading('Scrumban Overview',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Iterations
    para = sb_project.add_paragraph('Number of Iterations:')
    para.add_run('Number goes here').bold = True
    # WIP Limit
    para = sb_project.add_paragraph('Work In Progress Limit:')
    para.add_run('Number goes here').bold = True
    # Team 
    sb_project.add_heading('Team Structure',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Review
    sb_project.add_heading('Review Opportunities',level=1)
    sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
  

## Milestones ## 

    # Milestones table 
    sb_project.add_heading('Milestones',level=1)
    milestone_table = sb_project.add_table(rows=3, cols=2)
    milestone_table.style = 'LightShading-Accent1'
    header_cells = milestone_table.rows[0].cells
    header_cells[0].text = 'Milestone'
    header_cells[1].text = 'Date'
    row = milestone_table.add_row() # Method adding a row, to be called! 

    for row in table.rows:
        for cell in rows.cells:
            print(cell.text)

   # Delivery
    para = sb_project.add_paragraph('Delivery date:')
    para.add_run('Number goes here').bold = True

## Costs ## 

    # Invoice schedule table
    sb_project.add_heading('Invoice schedule',level=1)
    invoice_table = sb_project.add_table(rows=3, cols=3)
    invoice_table.style = 'LightShading-Accent1'
    header_cells = invoice_table.rows[0].cells
    header_cells[0].text = 'Invoice number'
    header_cells[1].text = 'Date'
    header_cells[2].text = 'Total'
    row = invoice_table.add_row() # Method adding a row, to be called! 

    for row in table.rows:
        for cell in rows.cells:
            print(cell.text)

## Acceptance ##

    # Signature 1
    sb_project.add_heading('Acceptance',level=1)
    sb_project.add_paragraph('Full name:', style=body_text_style)
    sb_project.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = sb_project.add_paragraph('Date signed:')
    para.add_run('Number goes here')
    # Signature 2
    sb_project.add_paragraph('Full name:', style=body_text_style)
    paragraph.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = sb_project.add_paragraph('Date signed:')
    para.add_run('Number goes here')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=ScrumbanProject.docx'
    sb_project.save(response)
    return response
