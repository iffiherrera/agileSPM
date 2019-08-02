from django.contrib import admin
from agileSPM.models import SOW, Scrum, Kanban, Scrumban

class Sow_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(SOW, Sow_admin)
admin.site.register(Scrum)
admin.site.register(Kanban)
admin.site.register(Scrumban)


