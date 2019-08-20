from django.contrib import admin
from . import models
from .models import SOWScrum, SOWKanban, SOWScrumban, UserProfile
    
admin.site.register(models.SOWScrum)
admin.site.register(models.SOWKanban)
admin.site.register(models.SOWScrumban)
admin.site.register(models.UserProfile)


