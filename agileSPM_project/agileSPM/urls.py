from django.conf.urls import url
from django.urls import path
from agileSPM import views
from .views import scrumForm, Edit_scrum_form, Delete_scrum_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django import forms
from agileSPM.preview import SOWScrumPreview
from .models import SOWKanban, SOWScrum, SOWScrumban

urlpatterns = [
    path('',views.index, name='index'),
    path('my_docs/', views.my_docs, name='my_docs'),
    path('register/',views.register, name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('restricted/', views.restricted, name='restricted'),
    path('scrum_form/' , views.scrumForm, name='scrum_form'),
    path('scrum_form//delete/<int:pk>/', Delete_scrum_form.as_view(), name='sow_form_delete'),
    path('scrum_form/edit/<int:pk>/', Edit_scrum_form.as_view(), name="edit_scrum_form"),
    path('success/<int:id>/', views.success, name='success'),
    path('scrum_doc/<int:id>/', views.scrum_doc, name='scrum_doc'),
    path('kanban_doc/<int:id>/', views.kanban_doc, name='kanban_doc'),
    path('scrumban_doc/<int:id>/', views.scrumban_doc, name='scrumban_doc'),

    # url(r'^$', views.index, name='index'),
    # # User account
    # url(r'^my_docs/', views.my_docs, name='my_docs'),
    # # Registration
    # url(r'^register/$', views.register, name='register'),
    # Scrum form view
    # url(r'^sow_scrum/$',Scrum_Sow_Wizard.as_view([CoverScrum1,IntroScrum2,ObjectivesScrum3,ScopeScrum4,BacklogScrum5,
    #                                                 ScrumForm6, MilestonesScrum7, CostScrum8, AcceptanceScrum9])),
    # # Kanban form view
    # url(r'^sow_kanban/$',Kanban_Sow_Wizard.as_view([CoverKanban1,IntroKanban2,ObjectivesKanban3,ScopeKanban4,BacklogKanban5,
    #                                                 KanbanForm6,MilestonesKanban7,CostKanban8,AcceptanceKanban9])),
    # # Scrumban form view
    # url(r'^sow_scrumban/$',Scrumban_Sow_Wizard.as_view([CoverScrumban1,IntroScrumban2,ObjectivesScrumban3,ScopeScrumban4,BacklogScrumban5,
    #                                                 ScrumbanForm6,MilestonesScrumban7,CostScrumban8,AcceptanceScrumban9])),
    # url(r'^form/$', views.fullForm, name='full_form'),
    # url(r'^success/$', views.success, name='success'),
    # url(r'^post/$',SOWScrumPreview(SOWScrum)),
    # url(r'^scrum_doc/', views.scrum_doc, name='scrum_doc'),
    # url(r'^kanban_doc/', views.kanban_doc, name='kanban_doc'),
    # url(r'^scrumban_doc/', views.scrumban_doc, name='scrumban_doc'),
]
