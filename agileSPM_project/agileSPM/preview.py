from formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from .models import SOWScrum, SOWKanban, SOWScrumban


# Form preview of before proceeding to download

class SOWScrumPreview(FormPreview):
    preview_template = "agileSPM/wizard/scrum_sow_template.html"
    model = SOWScrum
    def done (self, request, cleaned_data):
        title_scrum = cleaned_data[0]['title']
        produced_scrum = cleaned_data[0]['produced_by']
        date_scrum = cleaned_data[0]['date_project']
        
        return HttpResponseRedirect('/agileSPM/done.html')