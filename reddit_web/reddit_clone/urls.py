"""
URL configuration for reddit_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('reddit_clone.urls')),  # Inclui as URLs do app 'meu_app'
    
   
        
] + static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)

# meu_app/urls.py
urlpatterns = [
    path('', views.index, name='home'),  # Associa a URL raiz à função 'home'
    path('view_all/', views.view_all, name='view_all'),
    path('aba_comunidade/', views.aba_comunidade, name='aba_comunidade'),
   
]