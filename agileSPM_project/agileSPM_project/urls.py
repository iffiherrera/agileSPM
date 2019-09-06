"""agileSPM_project URL Configuration

"""
from django.contrib import admin
from django.urls import include, path
from agileSPM import views as views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),
    path('agileSPM/', include('agileSPM.urls')),
    path('agileSPM/', include('django.contrib.auth.urls')),
    path('admin/',admin.site.urls),

    # login, logout and register set in the project's urls folder to be accesible across the site
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    
# sets any uploaded documents to the media folder of this project.  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


