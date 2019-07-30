from django.conf.urls import url
from agileSPM import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sow_scrum/', views.sow_scrum, name='scrum'),
    url(r'^sow_kanban/', views.sow_kanban, name='kanban'),
    url(r'^sow_scrumban/', views.sow_scrumban, name='scrumban'),
    url(r'^my_docs/', views.my_docs, name='docs'),
    
]