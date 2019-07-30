from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage' : "checking index"}
    return render(request, 'agileSPM/index.html',context=context_dict)

def sow_scrum(request):
    context_dict = {'message2' : "scrum check"}
    return render(request, 'agileSPM/scrum.html', context=context_dict)

def sow_kanban(request):
    context_dict = {'message3' : "kanban check"}
    return render(request, 'agileSPM/kanban.html', context=context_dict)

def sow_scrumban(request):
    context_dict = {'message4' : "scrumban check"}
    return render(request, 'agileSPM/scrumban.html', context=context_dict)

def my_docs(request):
    context_dict = {'message5' : "docs check"}
    return render(request, 'agileSPM/docs.html', context=context_dict)


