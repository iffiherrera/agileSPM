from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from .models import SOWScrum, SOWKanban, SOWScrumban, User
from .forms import SOWScrumForm, EditScrumForm, SignUpModalForm, RegisterForm
from formtools.wizard.views import WizardView, SessionWizardView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView


# BS modal sign up pop up 
class ModalSignUpView(BSModalCreateView):
    form_class = SignUpModalForm
    template_name = 'agileSPM/register.html'
    success_url = reverse_lazy('my_docs')

def register(request):

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            print('username was succesful', username)
            return redirect('my_docs')
    else:
        register_form = RegisterForm()

    return render(request,'agileSPM/register.html', {'register_form' : register_form})


# Scrum form 
@login_required
def scrumForm(request):
    form = SOWScrumForm()

    if request.method == 'POST':
        form = SOWScrumForm(data=request.POST)

        if form.is_valid(): 
            form = form.save(commit=False)
            form.author = request.user
            print('user', request.user)
            # form.datetime.now()   
            # print(form.datetime)
            form.save()
            id = form.id
            print('id created:', id)
            return redirect('success', id=id)

        else:
            print(form.errors)
    
    else:
        form = SOWScrumForm()
    
    context_dict = {'user': request.user,
                    'form': form}

    return render(request,'agileSPM/full_form.html', context=context_dict)

# Successful completion of form view.
def success(request, id):
    complete_scrum_forms = SOWScrum.objects.filter(author=request.user)
    context_dict = {'id': id,
                    'complete_scrum_forms': complete_scrum_forms}

    return render(request,'agileSPM/wizard/done.html', context=context_dict)

# Home view 
def index(request):
    user_form = RegisterForm()
    context_dict = {
        'user': request.user,
        'user_form': user_form,
    }
    return render(request, 'agileSPM/index.html', context=context_dict)

# User account view 

def my_docs(request):
    user_scrum_forms = SOWScrum.objects.filter(author=request.user)
    print(user_scrum_forms)

    context_dict = {'user': request.user,
                    'id': id,
                    'user_scrum_forms': user_scrum_forms }
   
    print(request.user)

    return render(request, 'agileSPM/docs.html', context=context_dict)

## View to allow user to edit existing data populated in the specific document id.
class Edit_scrum_form(UpdateView):

    model = SOWScrum
    template_name = 'agileSPM/edit_sow_scrum.html'
    fields = ['title','produced_by','date_project',
                    'intro','deliverables','assumptions','inScope','outScope',
                    'backlog','sprintLength','sprint','team','done',
                    'review','milestones', 'milestone_description','delivery','invoice',
                    'invoice','invoice_info','amount','firstName',
                    'date_signature1','secondName','date_signature2',]

    def form_valid(self, form):
        print('object',form)
        self.object = form.save(commit=False)
        self.object.save()
        id = form.auto_id
        return redirect('edit_success', id=id)
        # print('Edit successful', pk)
       
        return super().form_valid(form)

def edit_success(request, id):
    edited_scrum_forms = SOWScrum.objects.filter(author=request.user)
    context_dict = {'id': id,
                    'edited_scrum_forms': edited_scrum_forms}

    return render(request,'agileSPM/edit.html', context=context_dict)

class Delete_scrum_form(DeleteView):
    model = SOWScrum
    success_url = reverse_lazy('agileSPM/my_docs')
  
# Scrum Document creation using docx-Python API
def scrum_doc(request, id):
    user_input = SOWScrum.objects.get(id=id)
    
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
    s_project.add_paragraph(milestones, style=list_bullet_style)
    s_project.add_paragraph(user_input.milestone_description, style=body_text_style)
    # milestone_table = s_project.add_table(rows=3, cols=2)
    # milestone_table.style = 'LightShading-Accent1'
    # header_cells = milestone_table.rows[0].cells
    # header_cells[0].text = 'Milestone'
    # header_cells[1].text = 'Date'
    # row = milestone_table.add_row() # Method adding a row, to be called! 
    # Delivery
    para = s_project.add_paragraph('Delivery date:')
    para.add_run(delivery).bold = True

    # for row in milestone_table.rows:
    #     for cell in row.cells:
    #         print(cell.text)

## Costs ## 

    # Invoice schedule table
    s_project.add_heading('Invoice schedule',level=1)
    s_project.add_paragraph(invoice, style=body_text_style)
    s_project.add_paragraph(user_input.invoice_info, style=body_text_style)
    # invoice_table = s_project.add_table(rows=3, cols=3)
    # invoice_table.style = 'LightShading-Accent1'
    # header_cells = invoice_table.rows[0].cells
    # header_cells[0].text = 'Invoice number'
    # header_cells[1].text = 'Date'
    # header_cells[2].text = 'Total'
    # row = invoice_table.add_row() # Method adding a row, to be called! 

    # for row in invoice_table.rows:
    #         for cell in row.cells:
    #             print(cell.text)

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
