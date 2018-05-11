
from django.urls import path
from .views import (
    novo_aluno, editar_aluno, excluir_aluno, pesquisar_aluno,
    pesquisar_coordenador, novo_coordenador, editar_coordenador, excluir_coordenador,
    message_list, message_create, message_edit, message_delete,
    novo_professor, editar_professor, excluir_professor, pesquisar_professor
)

urlpatterns = [
    path('incluirAluno/', novo_aluno),
    path('editarAluno/<int:id>/', editar_aluno),
    path('excluirAluno/<int:id>/', excluir_aluno),
    path('pesquisarAluno/', pesquisar_aluno),

    path('mensagens/', message_list, name='message_list'),
    path('mensagens/nova/', message_create, name='message_create'),
    path('mensagens/<int:pk>/editar', message_edit, name='message_edit'),
    path('mensagens/remover', message_delete, name='message_delete'),

    path('incluirProfessor/', novo_professor),
    path('editarProfessor/<int:id>/', editar_professor),
    path('excluirProfessor/<int:id>/', excluir_professor),
    path('pesquisarProfessor/', pesquisar_professor),

    path('pesquisarCoordenador/', pesquisar_coordenador),
    path('novoCoordenador/', novo_coordenador),
    path('editarCoordenador/<int:id>/', editar_coordenador),
    path('excluirCoordenador/<int:id>/', excluir_coordenador)
    ]
