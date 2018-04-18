"""refactorLMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from .views import (
    index, sobre, cursos, contato, login, disciplinaADS,
    novaDisciplina, novoAluno, novoCurso, matricula, ads, adm
)

urlpatterns = [
    path('', index),
    path('sobre/', sobre),
    path('cursos/', cursos),
    path('contato/', contato),
    path('login/', login),
    path('disciplinaADS/', disciplinaADS),
    path('novaDisciplina/', novaDisciplina),
    path('novoAluno/', novoAluno),
    path('novoCurso/', novoCurso),
    path('matricula/', matricula),
    path('ADS/', ads),
    path('ADM/', adm)
]
