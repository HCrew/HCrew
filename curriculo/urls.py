from django.urls import path
from .views import (
    novo_curso, editar_curso, excluir_curso, pesquisar_curso, pesquisar_disciplinas,
    nova_disciplina, editar_disciplina, excluir_disciplina, visualizar_disciplina)

urlpatterns = [
    path('incluirCurso/', novo_curso),
    path('editarCurso/<int:id>/', editar_curso),
    path('excluirCurso/<int:id>/', excluir_curso),
    path('pesquisarCurso/', pesquisar_curso),

    path('vizualizarDisciplina/<int:id>', visualizar_disciplina),
    path('pesquisarDisciplinas/', pesquisar_disciplinas),
    path('novaDisciplina/', nova_disciplina),
    path('editarDisciplina/<int:id>/', editar_disciplina),
    path('excluirDisciplina/<int:id>/', excluir_disciplina),

    ]
