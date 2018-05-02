
from django.urls import path
from .views import (
    novoAluno, editarAluno, excluirAluno, pesquisarAluno,
    pesquisarCoordenador, novoCoordenador, editarCoordenador
)

urlpatterns = [
    path('incluirAluno/', novoAluno),
    path('editarAluno/<int:id>/', editarAluno),
    path('excluirAluno/', excluirAluno),
    path('pesquisarAluno/', pesquisarAluno),
    path('pesquisarCoordenador/', pesquisarCoordenador),
    path('novoCoordenador/', novoCoordenador),  
    path('editarCoordenador/<int:id>/', editarCoordenador)
    ]
