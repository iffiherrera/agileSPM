from django.shortcuts import render
from django.http import HttpResponse
from docx import Document
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
    document = Document()
    document.add_heading('Document Title', 0)
    paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
    paragraph.add_run('bold').bold = True
    document.add_heading('Heading, level 1',level=1)
    document.add_paragraph('intense quote', style='IntenseQuote')

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'qty'
    hdr_cells[1].text = 'id'
    hdr_cells[2].text = 'desc'

    document.add_page_break()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=ScrumProject.docx'
    document.save(response)
    return response

