"""
URL configuration for linea_arbolgenealogico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'genealogia'

urlpatterns = [
    path('persona_form/', views.persona_form, name='persona_form'),
    path('parentesco_form/', views.parentesco_form, name='parentesco_form'),
    path('matrimonio_form/', views.matrimonio_form, name='matrimonio_form'),
    path('buscar_persona/', views.buscar_persona, name='buscar_persona'),
]
