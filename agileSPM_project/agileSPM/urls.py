from django.conf.urls import url
from django.urls import path
from agileSPM import views
from .views import scrumForm, scrumForm_update, DeleteScrumForm, DeleteKanbanForm, DeleteScrumbanForm, scrum_success
from .views import kanbanForm, scrumbanForm, kanbanForm_update, scrumbanForm_update, success_kanban, success_scrumban
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django import forms
from .models import SOWKanban, SOWScrum, SOWScrumban

urlpatterns = [
    path('',views.index, name='index'),
    path('my_docs/', views.my_docs, name='my_docs'),
    path('contact/', views.contact, name='contact'),
    

    # Scrum specific URLs
    path('scrum_form/' , views.scrumForm, name='scrum_form'),
    path('scrum_form/delete/<int:pk>/', DeleteScrumForm.as_view(), name='scrum_form_delete'),
    path('scrum_form/update/<int:id>/', views.scrumForm_update, name='scrum_update'),
    path('scrum_doc/<int:id>/', views.scrum_doc, name='scrum_doc'),
    path('scrum_success/<int:id>/', views.scrum_success, name='scrum_success'),
    # path('scrum_form/edit/<int:pk>/', Edit_scrum_form.as_view(), name="edit_scrum_form"),
    # path('edit_success_scrum/<int:id>/', views.edit_success_scrum, name='edit_success_scrum'),
    
    #Kanban specific URLs
    path('kanban_form/' , views.kanbanForm, name='kanban_form'),
    path('kanban_form/delete/<int:pk>/', DeleteKanbanForm.as_view(), name='kanban_form_delete'),
    path('kanban_form/edit/<int:id>/', views.kanbanForm_update, name="kanban_update"),
    path('kanban_success/<int:id>/', views.success_kanban, name='success_kanban'),
    path('kanban_doc/<int:id>/', views.kanban_doc, name='kanban_doc'),
    # path('edit_success_kanban/<int:id>/', views.edit_success_kanban, name='edit_success_kanban'),
    
    

    #Scrumban specific URLs
    path('scrumban_form/' , views.scrumbanForm, name='scrumban_form'),
    path('scrumban_form/delete/<int:pk>/', DeleteScrumbanForm.as_view(), name='scrumban_form_delete'),
    path('scrumban_form/edit/<int:id>/', views.scrumbanForm_update, name="scrumban_update"),
    path('scrumban_success/<int:id>/', views.success_scrumban, name='success_scrumban'),
    path('scrumban_doc/<int:id>/', views.scrumban_doc, name='scrumban_doc'),
]
