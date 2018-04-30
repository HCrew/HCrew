
from django.urls import path
from .views import (
    novoAluno, editarAluno, excluirAluno, pesquisarAluno
)

urlpatterns = [
    path('incluirAluno/', novoAluno),
    path('editarAluno/<int:id>/', editarAluno),
    path('excluirAluno/', excluirAluno),
    path('pesquisarAluno/', pesquisarAluno)
]