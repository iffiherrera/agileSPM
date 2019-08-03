from django.contrib import admin
from .models import SOW, Scrum, Kanban, Scrumban, UserProfile

class Sow_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(SOW, Sow_admin)
admin.site.register(Scrum)
admin.site.register(Kanban)
admin.site.register(Scrumban)
admin.site.register(UserProfile)


