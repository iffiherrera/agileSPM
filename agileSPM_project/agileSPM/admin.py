from django.contrib import admin
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import SOWScrum, SOWKanban, SOWScrumban

admin.site.register(models.SOWScrum)
admin.site.register(models.SOWKanban)
admin.site.register(models.SOWScrumban)



