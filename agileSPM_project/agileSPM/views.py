from django.shortcuts import render
from django.http import HttpResponse
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from agileSPM import models


# Home view 
def index(request):  
    return render(request, 'agileSPM/index.html')
   
# Scrum view
def sow_scrum(request):
    context_dict = {'message2' : "scrum check"}
    return render(request, 'agileSPM/scrum.html', context=context_dict)

# Kanban view
def sow_kanban(request):
    context_dict = {'message3' : "kanban check"}
    return render(request, 'agileSPM/kanban.html', context=context_dict)

# Scrumban view
def sow_scrumban(request):
    context_dict = {'message4' : "scrumban check"}
    return render(request, 'agileSPM/scrumban.html', context=context_dict)

# User account view 
def my_docs(request):
    context_dict = {'message5' : "docs check"}
    return render(request, 'agileSPM/docs.html', context=context_dict)

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

## Cover page ##

    # Title
    s_project.add_heading('Scrum Project', 0)
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
