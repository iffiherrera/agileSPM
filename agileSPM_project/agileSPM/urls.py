from django.conf.urls import url
from agileSPM import views
# from agileSPM.views import Scrum_Sow_Wizard, Kanban_Sow_Wizard, Scrumban_Sow_Wizard
from .views import Scrum_Sow_Wizard, Kanban_Sow_Wizard, Scrumban_Sow_Wizard
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import CoverScrum1,IntroScrum2,ObjectivesScrum3,ScopeScrum4,BacklogScrum5,ScrumForm6, MilestonesScrum7, CostScrum8, AcceptanceScrum9
from .forms import CoverKanban1, IntroKanban2, ObjectivesKanban3, ScopeKanban4, BacklogKanban5, KanbanForm6, MilestonesKanban7, CostKanban8, AcceptanceKanban9
from .forms import CoverScrumban1, IntroScrumban2, ObjectivesScrumban3, ScopeScrumban4, BacklogScrumban5, ScrumbanForm6, MilestonesScrumban7, CostScrumban8, AcceptanceScrumban9


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # User account
    url(r'^my_docs/', views.my_docs, name='my_docs'),
    # Registration
    url(r'^register/$', views.register, name='register'),
    # Scrum form view
    url(r'^sow_scrum/$',Scrum_Sow_Wizard.as_view([CoverScrum1,IntroScrum2,ObjectivesScrum3,ScopeScrum4,BacklogScrum5,
                                                    ScrumForm6, MilestonesScrum7, CostScrum8, AcceptanceScrum9])),
    # Kanban form view
    url(r'^sow_kanban/$',Kanban_Sow_Wizard.as_view([CoverKanban1,IntroKanban2,ObjectivesKanban3,ScopeKanban4,BacklogKanban5,
                                                    KanbanForm6,MilestonesKanban7,CostKanban8,AcceptanceKanban9])),
    # Scrumban form view
    url(r'^sow_scrumban/$',Scrumban_Sow_Wizard.as_view([CoverScrumban1,IntroScrumban2,ObjectivesScrumban3,ScopeScrumban4,BacklogScrumban5,
                                                    ScrumbanForm6,MilestonesScrumban7,CostScrumban8,AcceptanceScrumban9])),
    url(r'^scrum_doc/', views.scrum_doc, name='scrum_doc'),
    url(r'^kanban_doc/', views.kanban_doc, name='kanban_doc'),
    url(r'^scrumban_doc/', views.scrumban_doc, name='scrumban_doc'),
    
]
