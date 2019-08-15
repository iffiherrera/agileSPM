from django.contrib import admin
from .models import SOWScrum, SOWKanban, SOWScrumban, UserProfile

class Sow_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(SOWScrum, Sow_admin)
admin.site.register(SOWKanban)
admin.site.register(SOWScrumban)
admin.site.register(UserProfile)


