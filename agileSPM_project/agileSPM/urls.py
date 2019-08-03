from django.conf.urls import url
from agileSPM import views
from agileSPM.views import Scrum_Sow_Wizard, Kanban_Sow_Wizard, Scrumban_Sow_Wizard
from .views import SCRUM_FORM, Scrum_Sow_Wizard, Kanban_Sow_Wizard, Scrumban_Sow_Wizard
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import CoverForm1,IntroForm2,ObjectivesForm3,ScopeForm4,BacklogForm5,ScrumForm6
from .forms import KanbanForm6, ScrumbanForm6, MilestonesForm7, CostForm8, AcceptanceForm9


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^sow_scrum/(?P<sow_slug_title>[\w\-]+)/$', views.sow_scrum, name='scrum'),
    # url(r'^sow_scrum_view/(?P<step>.+)/$', views.sow_scrum_view, name='scrum_step'),
    # url(r'^sow_scrum_view/$',views.sow_scrum_view,name='scrum'),
    url(r'^my_docs/', views.my_docs, name='docs'),
    # Scrum form view
    url(r'^sow_scrum/$',Scrum_Sow_Wizard.as_view([CoverForm1,IntroForm2,ObjectivesForm3,ScopeForm4,BacklogForm5,
                                                    ScrumForm6,MilestonesForm7,CostForm8,AcceptanceForm9])),
    # Kanban form view
    url(r'^sow_kanban/$',Kanban_Sow_Wizard.as_view([CoverForm1,IntroForm2,ObjectivesForm3,ScopeForm4,BacklogForm5,
                                                    KanbanForm6,MilestonesForm7,CostForm8,AcceptanceForm9])),
    # Scrumban form view
    url(r'^sow_scrumban/$',Scrumban_Sow_Wizard.as_view([CoverForm1,IntroForm2,ObjectivesForm3,ScopeForm4,BacklogForm5,
                                                    ScrumbanForm6,MilestonesForm7,CostForm8,AcceptanceForm9])),
    url(r'^scrum_doc/', views.scrum_doc, name='scrum_doc'),
    url(r'^kanban_doc/', views.kanban_doc, name='kanban_doc'),
    url(r'^scrumban_doc/', views.scrumban_doc, name='scrumban_doc'),
    
]
