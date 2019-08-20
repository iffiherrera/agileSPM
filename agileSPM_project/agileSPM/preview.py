from formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from .models import SOWScrum, SOWKanban, SOWScrumban
from .forms import CoverScrum1, IntroScrum2, ObjectivesScrum3, ScopeScrum4, ScrumForm6, BacklogScrum5, MilestonesScrum7, CostScrum8, AcceptanceScrum9, UserForm, UserProfileForm
from .forms import CoverKanban1, IntroKanban2, ObjectivesKanban3, ScopeKanban4, BacklogKanban5, KanbanForm6, MilestonesKanban7, CostKanban8, AcceptanceKanban9
from .forms import CoverScrumban1, IntroScrumban2, ObjectivesScrumban3, ScopeScrumban4, BacklogScrumban5, ScrumbanForm6, MilestonesScrumban7, CostScrumban8, AcceptanceScrumban9


# Form preview of before proceeding to download

class SOWScrumPreview(FormPreview):
    preview_template = "agileSPM/wizard/scrum_sow_template.html"
    model = SOWScrum
    def done (self, request, cleaned_data):
        title_scrum = cleaned_data[0]['title']
        produced_scrum = cleaned_data[0]['produced_by']
        date_scrum = cleaned_data[0]['date_project']
        
        return HttpResponseRedirect('/agileSPM/done.html')