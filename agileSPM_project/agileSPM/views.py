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

## Document formatting and rules ##
    s_project = Document()

    paragraph = s_project.add_paragraph()
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.keep_with_next = True

    styles = s_project.styles
    body_text_style = s_project.styles['Body Text']
    list_bullet_style = s_project.styles['List Bullet']
    numbered_bullet_style = s_project.styles['ListNumber']

## ADD TABLE STYLING ######

## Cover page ##

    # Title
    s_project.add_heading('Scrum Project', 0)
    # Produced by 
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Date created
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    s_project.add_page_break()

## Overview ##

    # Introduction
    s_project.add_heading('Introduction', level=1)
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Objectives ##

    # Deliverables 
    s_project.add_heading('Deliverables',level=1)
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)
    # Assumptions
    s_project.add_heading('Assumptions',level=1)
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Scope ##

    # In Scope
    s_project.add_heading('In Scope',level=1)
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Out of Scope
    s_project.add_heading('Out of Scope',level=1)
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Backlog ##

    # Product backlog 
    s_project.add_heading('Product backlog',level=1)
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## ADD IN SCRUM SPECIFIC STUFF HERE ########

## Milestones ## 

    # Milestones table 
    s_project.add_heading('Milestones',level=1)
    milestone_table = s_project.add_table(rows=3, cols=2)
    header_cells = milestone_table.rows[0].cells
    header_cells[0].text = 'Milestone'
    header_cells[1].text = 'Date'
    row = milestone_table.add_row() # Method adding a row, to be called! 
    # Delivery
    s_project.add_heading('Delivery date',level=1)
    paragraph = s_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Costs ## 

    # Invoice schedule table
    s_project.add_heading('Invoice schedule',level=1)
    invoice_table = s_project.add_table(rows=3, cols=3)
    header_cells = invoice_table.rows[0].cells
    header_cells[0].text = 'Invoice number'
    header_cells[1].text = 'Date'
    header_cells[2].text = 'Total'
    row = invoice_table.add_row() # Method adding a row, to be called! 

## Acceptance ##

    s_project.add_heading('Acceptance',level=1)
    paragraph = s_project.add_paragraph('Full name:', style=body_text_style)
    s_project.add_paragraph('Signature:', style='IntenseQuote')

    paragraph = s_project.add_paragraph('Full name:', style=body_text_style)
    s_project.add_paragraph('Signature:', style='IntenseQuote')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=ScrumProject.docx'
    s_project.save(response)
    return response

# Kanban Document creation using docx-Python API
def kanban_doc(request):

## Document formatting and rules ##
    k_project = Document()

    paragraph = k_project.add_paragraph()
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.keep_with_next = True

    styles = k_project.styles
    body_text_style = k_project.styles['Body Text']
    list_bullet_style = k_project.styles['List Bullet']
    numbered_bullet_style = k_project.styles['ListNumber']

## ADD TABLE STYLING ######

## Cover page ##

    # Title
    k_project.add_heading('Scrum Project', 0)
    # Produced by 
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Date created
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    k_project.add_page_break()

## Overview ##

    # Introduction
    k_project.add_heading('Introduction', level=1)
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Objectives ##

    # Deliverables 
    k_project.add_heading('Deliverables',level=1)
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)
    # Assumptions
    k_project.add_heading('Assumptions',level=1)
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Scope ##

    # In Scope
    k_project.add_heading('In Scope',level=1)
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Out of Scope
    k_project.add_heading('Out of Scope',level=1)
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Backlog ##

    # Product backlog 
    k_project.add_heading('Product backlog',level=1)
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## ADD IN SCRUM SPECIFIC STUFF HERE ########

## Milestones ## 

    # Milestones table 
    k_project.add_heading('Milestones',level=1)
    milestone_table = k_project.add_table(rows=3, cols=2)
    header_cells = milestone_table.rows[0].cells
    header_cells[0].text = 'Milestone'
    header_cells[1].text = 'Date'
    row = milestone_table.add_row() # Method adding a row, to be called! 
    # Delivery
    k_project.add_heading('Delivery date',level=1)
    paragraph = k_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Costs ## 

    # Invoice schedule table
    k_project.add_heading('Invoice schedule',level=1)
    invoice_table = k_project.add_table(rows=3, cols=3)
    header_cells = invoice_table.rows[0].cells
    header_cells[0].text = 'Invoice number'
    header_cells[1].text = 'Date'
    header_cells[2].text = 'Total'
    row = invoice_table.add_row() # Method adding a row, to be called! 

## Acceptance ##

    k_project.add_heading('Acceptance',level=1)
    paragraph = k_project.add_paragraph('Full name:', style=body_text_style)
    k_project.add_paragraph('Signature:', style='IntenseQuote')

    paragraph = k_project.add_paragraph('Full name:', style=body_text_style)
    k_project.add_paragraph('Signature:', style='IntenseQuote')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=KanbanProject.docx'
    k_project.save(response)
    return response

# Scrumban Document creation using docx-Python API
def scrumban_doc(request):

## Document formatting and rules ##
    sb_project = Document()

    paragraph = sb_project.add_paragraph()
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.keep_with_next = True

    styles = sb_project.styles
    body_text_style = sb_project.styles['Body Text']
    list_bullet_style = sb_project.styles['List Bullet']
    numbered_bullet_style = sb_project.styles['ListNumber']

## ADD TABLE STYLING ######

## Cover page ##

    # Title
    sb_project.add_heading('Scrum Project', 0)
    # Produced by 
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Date created
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    sb_project.add_page_break()

## Overview ##

    # Introduction
    sb_project.add_heading('Introduction', level=1)
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Objectives ##

    # Deliverables 
    sb_project.add_heading('Deliverables',level=1)
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)
    # Assumptions
    sb_project.add_heading('Assumptions',level=1)
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## Scope ##

    # In Scope
    sb_project.add_heading('In Scope',level=1)
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)
    # Out of Scope
    sb_project.add_heading('Out of Scope',level=1)
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Backlog ##

    # Product backlog 
    sb_project.add_heading('Product backlog',level=1)
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=list_bullet_style)

## ADD IN SCRUM SPECIFIC STUFF HERE ########

## Milestones ## 

    # Milestones table 
    sb_project.add_heading('Milestones',level=1)
    milestone_table = sb_project.add_table(rows=3, cols=2)
    header_cells = milestone_table.rows[0].cells
    header_cells[0].text = 'Milestone'
    header_cells[1].text = 'Date'
    row = milestone_table.add_row() # Method adding a row, to be called! 
    # Delivery
    sb_project.add_heading('Delivery date',level=1)
    paragraph = sb_project.add_paragraph('Lorem ipsum dolor sit amet.', style=body_text_style)

## Costs ## 

    # Invoice schedule table
    sb_project.add_heading('Invoice schedule',level=1)
    invoice_table = sb_project.add_table(rows=3, cols=3)
    header_cells = invoice_table.rows[0].cells
    header_cells[0].text = 'Invoice number'
    header_cells[1].text = 'Date'
    header_cells[2].text = 'Total'
    row = invoice_table.add_row() # Method adding a row, to be called! 

## Acceptance ##

    sb_project.add_heading('Acceptance',level=1)
    paragraph = sb_project.add_paragraph('Full name:', style=body_text_style)
    sb_project.add_paragraph('Signature:', style='IntenseQuote')

    paragraph = sb_project.add_paragraph('Full name:', style=body_text_style)
    sb_project.add_paragraph('Signature:', style='IntenseQuote')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=ScrumbanProject.docx'
    sb_project.save(response)
    return response
