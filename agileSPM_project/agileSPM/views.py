from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from .models import SOWScrum, SOWKanban, SOWScrumban, UserProfile, User
from .forms import SOWScrumForm, UserForm, EditScrumForm
from formtools.wizard.views import WizardView, SessionWizardView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView


# Login pop up 

class login_view(BSModalCreateView):
    template_name = 'agileSPM/register.html'
    form_class = UserForm
    success_message = 'Thank you for registering.'
    success_url = reverse_lazy('index')


# Scrum form 
def fullForm(request):
    form = SOWScrumForm()

    if request.method == 'POST':
        form = SOWScrumForm(data=request.POST)

        if form.is_valid(): 
            form = form.save(commit=False)
            
        
            # form.datetime.now()   
            form.save()
            id = form.id
            return redirect('success', id=id)

        else:
            print(form.errors)
    
    else:
        form = SOWScrumForm()
    
    return render(request,'agileSPM/full_form.html', {'form' : form})


# Successful completion of form view.
def success(request, id):
    context_dict = {'id': id}
    return render(request,'agileSPM/wizard/done.html', context=context_dict)

# Home view 
def index(request):
    user_form = UserForm()

    context_dict = {
        'user_form': user_form,
    }
    return render(request, 'agileSPM/index.html', context=context_dict)

# User account view 
# @login_required()
def my_docs(request):
    context_dict = {'user': request.user,
                    'id': id }
   
    print(request.user)

    return render(request, 'agileSPM/docs.html', context=context_dict)

def edit_scrum_form(request,id):
    scrum_form = SOWScrum.objects.get(id=id)
    editable_form = EditScrumForm(instance=scrum_form)

    if request.method == 'POST':
        form = EditScrumForm(request.POST)

        if form.is_valid():
            # title
            title_update = form.cleaned_data['title']
            scrum_form.title = title_update
            
            
            #produced by 
            produced_update = form.cleaned_data['produced_by']
            scrum_form.produced_by = produced_update
            

            # scrum.date_project = form.cleaned_data['date_project']
            # scrum_form.title = title_update
            # scrum.intro = form.cleaned_data['intro']
            # scrum_form.title = title_update
            # scrum.deliverables = form.cleaned_data['deliverables']
            # scrum_form.title = title_update
            # scrum.assumptions = form.cleaned_data['assumptions']
            # scrum_form.title = title_update
            # scrum.inScope = form.cleaned_data['inScope']
            # scrum_form.title = title_update
            # scrum.outScope = form.cleaned_data['outScope']
            # scrum_form.title = title_update
            # scrum.backlog = form.cleaned_data['backlog']
            # scrum_form.title = title_update
            # scrum.sprintLength = form.cleaned_data['sprintLength']
            # scrum_form.title = title_update
            # scrum.sprint = form.cleaned_data['sprint']
            # scrum_form.title = title_update
            # scrum.sprintPlan = form.cleaned_data['sprintPlan']
            # scrum_form.title = title_update
            # scrum.team = form.cleaned_data['team']
            # scrum_form.title = title_update
            # scrum.done = form.cleaned_data['done']
            # scrum_form.title = title_update
            # scrum.review = form.cleaned_data['review']
            # scrum_form.title = title_update
            # scrum.milestones = form.cleaned_data['milestones']
            # scrum_form.title = title_update
            # scrum.milestone_description = form.cleaned_data['milestone_desription']
            # scrum_form.title = title_update
            # scrum.delivery = form.cleaned_data['delivery']
            # scrum_form.title = title_update
            # scrum.invoice = form.cleaned_data['invoice']
            # scrum_form.title = title_update
            # scrum.invoice_info = form.cleaned_data['invoice_info']
            # scrum_form.title = title_update
            # scrum.amount = form.cleaned_data['amount']
            # scrum_form.title = title_update
            # scrum.firstName = form.cleaned_data['firstName']
            # scrum_form.title = title_update
            # scrum.date_signature1 = form.cleaned_data['date_signature1']
            # scrum_form.title = title_update
            # scrum.secondName = form.cleaned_data['secondName']
            # scrum_form.title = title_update
            # scrum.date_signature2 = form.cleaned_data['date_signature2']
            # scrum_form.title = title_update


            scrum_form.updated = datetime.now()
            scrum_form.save()


# Pop up login/sign up function using Ajax function and modal, returning a JSON response.
# def login_popup(request):
#     context_dict = {}
#     if request.method == 'POST':
#         # Request and validate username/password.
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return JsonResponse({'login': True})
#             else:
#                 context_dict['error'] = "Account is no longer active"
#                 return JsonResponse({'login': False,
#                                         'error': context_dict['error']})
#         else:
#             context_dict['error'] = "Username and password do not match. Please try again."
#             print("Invalid:{0},{1}".format(username,password))
#             return JsonResponse({'login': False,
#                                         'error': context_dict['error']})
#     else:
#         context_dict['action'] = 'login'
#         return render(request,'agileSPM/index.html', context=context_dict)

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
    
        # Saves user and profile input to database.
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True # Sets registration to true at this point.
            return redirect('my_docs')

        else:
            print(user_form.errors) # prints errors to terminal for testing/QA
    else:
        user_form = UserForm()
    print('succesful', request.user)
    return render(request, 'agileSPM/register.html', {'user_form' : user_form,
                                                       'registered' : registered,})    

# Scrum Document creation using docx-Python API
def scrum_doc(request, id):
    user_input = SOWScrum.objects.get(id=id)
    print('Date printed',user_input.date_project)

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

    # Casting datetime fields as string
    date = str(user_input.date_project)
    milestones = str(user_input.milestones)
    delivery = str(user_input.delivery)
    date_signature1 = str(user_input.date_signature1)
    date_signature2 = str(user_input.date_signature2)

    # Casting int values to string
    sprints = str(user_input.sprint)
    length = str(user_input.sprintLength)
    invoice = str(user_input.invoice)



## Cover page ##

    # Title
    s_project.add_heading(user_input.title, 0)
    # print(s_project)
    # Produced by 
    s_project.add_paragraph(user_input.produced_by, style=body_text_style)
    # Date created
    s_project.add_paragraph(date, style=body_text_style)
    s_project.add_page_break()

## Overview ##

    # Introduction
    s_project.add_heading('Introduction', level=1)
    s_project.add_paragraph(user_input.intro, style=body_text_style)

## Objectives ##

    # Deliverables 
    s_project.add_heading('Deliverables',level=1)
    s_project.add_paragraph(user_input.deliverables, style=list_bullet_style)
    # Assumptions
    s_project.add_heading('Assumptions',level=1)
    s_project.add_paragraph(user_input.assumptions, style=list_bullet_style)

## Scope ##

    # In Scope
    s_project.add_heading('In Scope',level=1)
    s_project.add_paragraph(user_input.outScope, style=body_text_style)
    # Out of Scope
    s_project.add_heading('Out of Scope',level=1)
    s_project.add_paragraph(user_input.inScope, style=body_text_style)

## Backlog ##

    # Product backlog 
    s_project.add_heading('Product backlog',level=1)
    s_project.add_paragraph(user_input.backlog, style=list_bullet_style)

## Mode of Delivery ##

    # Sprint plan 
    s_project.add_heading('Sprint Planning',level=1)
    s_project.add_paragraph(user_input.sprintPlan, style=body_text_style)
    # Sprints
    para = s_project.add_paragraph('Number of Sprints:')
    para.add_run(sprints).bold = True
    # Sprint Length
    para = s_project.add_paragraph('Length of Sprint:')
    para.add_run(length).bold = True
    # Team 
    s_project.add_heading('Team Structure',level=1)
    s_project.add_paragraph(user_input.team, style=body_text_style)
    # Done
    s_project.add_heading('Defining Done',level=1)
    s_project.add_paragraph(user_input.done, style=body_text_style)
    # Review
    s_project.add_heading('Review Opportunities',level=1)
    s_project.add_paragraph(user_input.review, style=body_text_style)
  

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
    para.add_run(delivery).bold = True

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
    para = s_project.add_paragraph('Full Name:')
    para.add_run(user_input.firstName).bold = True
    s_project.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = s_project.add_paragraph('Date signed:')
    para.add_run(date_signature1)
    # Signature 2
    para = s_project.add_paragraph('Full Name:')
    para.add_run(user_input.secondName).bold = True
    s_project.add_paragraph('Signature:', style='IntenseQuote')
    # Date
    para = s_project.add_paragraph('Date signed:')
    para.add_run(date_signature2)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=ScrumProject.docx'
    s_project.save(response)
    return response

    return render(request)

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
