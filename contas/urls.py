
from django.urls import path
from .views import (
    novoAluno, editarAluno, excluirAluno, pesquisarAluno,
    message_create, message_edit, message_delete, message_list,
    novoProfessor, editarProfessor, excluirProfessor, pesquisarProfessor
)

urlpatterns = [
    #Aluno
    path('incluirAluno/', novoAluno),
    path('editarAluno/<int:id>/', editarAluno),
    path('excluirAluno/<int:id>/', excluirAluno),
    path('pesquisarAluno/', pesquisarAluno),

    # Mensagens
    path('mensagens/', message_list, name='message_list'),
    path('mensagens/nova/', message_create, name='message_create'),
    path('mensagens/<int:pk>/editar', message_edit, name='message_edit'),
    path('mensagens/remover', message_delete, name='message_delete'),

    #Professor
    path('incluirProfessor/', novoProfessor),
    path('editarProfessor/<int:id>/', editarProfessor),
    path('excluirProfessor/', excluirProfessor),
    path('pesquisarProfessor/', pesquisarProfessor),

    #Mensagens
    path('mensagens/nova/', message_create, name = 'message_create'),
    path('mensagens/<int:pk>/editar', message_edit, name = 'message_edit'),
    path('mensagens/remover', message_delete, name = 'message_delete'),
    path('mensagens/', message_list, name = 'message_list'),
]