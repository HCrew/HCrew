from django.urls import path
from .views import ( pesquisarDisciplinas, novaDisciplina )

urlpatterns = [

path('pesquisarDisciplinas/', pesquisarDisciplinas),
path('novaDisciplina/', novaDisciplina)

]
