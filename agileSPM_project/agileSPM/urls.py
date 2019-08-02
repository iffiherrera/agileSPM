from django.conf.urls import url
from agileSPM import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sow_scrum/(?P<sow_slug_title>[\w\-]+)/$', views.sow_scrum, name='scrum'),
    url(r'^sow_kanban/', views.sow_kanban, name='kanban'),
    url(r'^sow_scrumban/', views.sow_scrumban, name='scrumban'),
    url(r'^my_docs/', views.my_docs, name='docs'),
    url(r'^scrum_doc/', views.scrum_doc, name='scrum_doc'),
    url(r'^kanban_doc/', views.kanban_doc, name='kanban_doc'),
    url(r'^scrumban_doc/', views.scrumban_doc, name='scrumban_doc'),
    
]