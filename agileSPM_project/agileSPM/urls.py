from django.conf.urls import url
from django.urls import path
from agileSPM import views
from .views import scrumForm, Edit_scrum_form, Delete_scrum_form, Edit_kanban_form, Edit_scrumban_form
from .views import Delete_scrumban_form, Delete_kanban_form, kanbanForm, scrumbanForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django import forms
from .models import SOWKanban, SOWScrum, SOWScrumban

urlpatterns = [
    path('',views.index, name='index'),
    path('my_docs/', views.my_docs, name='my_docs'),
    path('signup/', views.ModalSignUpView.as_view(), name='signup'),
    path('test/', views.test, name='test'),
    path('contact/', views.contact, name='contact'),

    # Scrum specific URLs
    path('scrum_form/' , views.scrumForm, name='scrum_form'),
    path('scrum_form//delete/<int:pk>/', Delete_scrum_form.as_view(), name='scrum_form_delete'),
    path('scrum_form/edit/<int:pk>/', Edit_scrum_form.as_view(), name="edit_scrum_form"),
    path('edit_success_scrum/<int:id>/', views.edit_success_scrum, name='edit_success_scrum'),
    path('scrum_success/<int:id>/', views.success_scrum, name='success_scrum'),
    path('scrum_doc/<int:id>/', views.scrum_doc, name='scrum_doc'),

    #Kanban specific URLs
    path('kanban_form/' , views.kanbanForm, name='kanban_form'),
    path('kanban_form//delete/<int:pk>/', Delete_kanban_form.as_view(), name='kanban_form_delete'),
    path('kanban_form/edit/<int:pk>/', Edit_kanban_form.as_view(), name="edit_kanban_form"),
    path('edit_success_kanban/<int:id>/', views.edit_success_kanban, name='edit_success_kanban'),
    path('kanban_success/<int:id>/', views.success_kanban, name='success_kanban'),
    path('kanban_doc/<int:id>/', views.kanban_doc, name='kanban_doc'),

    #Scrumban specific URLs
    path('scrumban_form/' , views.scrumbanForm, name='scrumban_form'),
    path('scrumban_form//delete/<int:pk>/', Delete_scrumban_form.as_view(), name='scrumban_form_delete'),
    path('scrumban_form/edit/<int:pk>/', Edit_scrumban_form.as_view(), name="edit_scrumban_form"),
    path('edit_success_scrumban/<int:id>/', views.edit_success_scrumban, name='edit_success_scrumban'),
    path('scrumban_success/<int:id>/', views.success_scrumban, name='success_scrumban'),
    path('scrumban_doc/<int:id>/', views.scrumban_doc, name='scrumban_doc'),
]
