
from django.urls import path
from .views import (
    novoAluno, editarAluno, excluirAluno, pesquisarAluno
)

urlpatterns = [
    path('novoAluno/', novoAluno),
    path('editarAluno/', editarAluno),
    path('excluirAluno/', excluirAluno),
    path('pesquisarAluno/', pesquisarAluno)
]